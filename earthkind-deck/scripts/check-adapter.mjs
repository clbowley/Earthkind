// Regression check against synthetic expected geometry; performs no network calls.
import fs from 'node:fs';
import assert from 'node:assert/strict';
import {applyEarthkindPlan} from './apply-native.mjs';
const root=new URL('../',import.meta.url);
const read=p=>JSON.parse(fs.readFileSync(new URL(p,root),'utf8'));
const base=read('validation/base-before.json'),expected=read('validation/verified.json'),plan=read('validation/plan.json');
let state=structuredClone(base),revision=base.revisionId,calls=0;
const elements=()=>state.slides.flatMap(s=>s.pageElements),lookup=id=>elements().find(e=>e.objectId===id);
const expectedById=Object.fromEntries(expected.slides.flatMap(s=>s.pageElements).map(e=>[e.objectId,e]));
const api={
 offlineFixture:true,
 getPresentation:async()=>({...structuredClone(state),revisionId:revision}),
 batchUpdate:async args=>{
  assert.equal(args.write_control.requiredRevisionId,revision);
  for(const request of args.requests){
   const [kind,v]=Object.entries(request)[0];
   if(kind==='deleteObject'){for(const s of state.slides)s.pageElements=s.pageElements.filter(e=>e.objectId!==v.objectId);continue;}
   if(kind==='createShape'||kind==='createImage'){
    assert(!lookup(v.objectId),'Duplicate '+v.objectId);
    const e={objectId:v.objectId,...structuredClone(v.elementProperties)};delete e.pageObjectId;
    if(kind==='createImage')e.image={sourceUrl:'https://example.test/upload/'+v.objectId};else e.shape={};
    state.slides.find(s=>s.objectId===v.elementProperties.pageObjectId).pageElements.push(e);continue;
   }
   if(kind==='replaceImage'){
    const e=lookup(v.imageObjectId);assert(e);e.image.sourceUrl='https://example.test/upload/'+v.imageObjectId;e.size=structuredClone(expectedById[v.imageObjectId].size);continue;
   }
   if(kind==='updatePageElementTransform'){assert(lookup(v.objectId));lookup(v.objectId).transform=structuredClone(v.transform);continue;}
   if(kind==='updatePageElementsZOrder'){for(const id of v.pageElementObjectIds)assert(lookup(id));continue;}
   if(kind==='updatePageProperties'){assert(state.slides.some(s=>s.objectId===v.objectId));continue;}
   assert(lookup(v.objectId),kind+' missing '+v.objectId);
   if(kind==='updateShapeProperties')assert(!v.fields.split(',').includes('autofit'),'Read-only autofit parent field');
  }
  revision='mock-'+(++calls);return {writeControl:{requiredRevisionId:revision}};
 }
};
await assert.rejects(()=>applyEarthkindPlan({plan,assetRoot:'/local/assets',api:{...api,offlineFixture:false}}),/offline-only/);
await assert.rejects(()=>applyEarthkindPlan({plan,assetRoot:'/local/assets',api,protectedPresentationIds:[plan.targetPresentationId]}),/read-only/);
await applyEarthkindPlan({plan,assetRoot:'/local/assets',api});
// Compare effective endpoint vectors in points, including zero-valued line axes.
let compared=0,maxError=0;
for(const e of elements()){
 const want=expectedById[e.objectId];if(!want)continue;
 const vector=x=>{
  const t=x.transform||{},w=x.size?.width?.magnitude||0,h=x.size?.height?.magnitude||0;
  return [(t.scaleX||0)*w,(t.shearY||0)*w,(t.shearX||0)*h,(t.scaleY||0)*h,t.translateX||0,t.translateY||0].map(n=>n/12700);
 };
 const a=vector(e),b=vector(want),err=Math.max(...a.map((v,i)=>Math.abs(v-b[i])));maxError=Math.max(maxError,err);assert(err<0.03,e.objectId+' geometry drift '+err);compared++;
}
console.log(JSON.stringify({status:'pass',mockBatches:calls,geometryObjectsCompared:compared,maxPointError:maxError,scope:'Synthetic offline executor regression only; no live Google API certification.'}));
