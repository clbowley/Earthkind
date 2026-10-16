/** Provider-neutral native Slides executor. No credentials or networking embedded.
 * api.getPresentation(id) -> native presentation JSON
 * api.batchUpdate({presentation_id, requests, image_uris?, write_control})
 *   -> native batchUpdate response. Unwrap your connector's structuredContent.
 * image_uris is one absolute local asset path; the connector uploads its bytes.
 * A plain REST adapter must implement an equivalent authenticated image upload.
 */
export async function applyEarthkindPlan({plan, assetRoot, api, protectedPresentationIds=[], onProgress=()=>{}}) {
  const id=plan.targetPresentationId;
  if(protectedPresentationIds.includes(id)) throw Error('Approved reference is read-only.');
  if(id.startsWith('SYNTHETIC_') && !api.offlineFixture) throw Error('Synthetic examples are offline-only.');
  let current=await api.getPresentation(id),revision=current.revisionId;
  if(revision!==plan.baseRevision) throw Error('Base changed after compilation. Re-read and recompile.');
  const urls=new Map();
  async function send(requests,imagePath) {
    const result=await api.batchUpdate({presentation_id:id,requests,...(imagePath?{image_uris:imagePath}:{}),write_control:{requiredRevisionId:revision}});
    if(result.error||!result.writeControl?.requiredRevisionId) throw Error(result.error||'Missing successful write control.');
    revision=result.writeControl.requiredRevisionId;
  }
  async function sendChunks(requests) {
    for(let i=0;i<requests.length;i+=150) await send(requests.slice(i,i+150));
  }
  for(const phase of plan.phases) {
    await sendChunks(phase.requests);
    for(const a of phase.assets) {
      const path=assetRoot.replace(/\/$/,'')+'/'+a.asset, cached=urls.get(a.asset),url=cached||path;
      const request=a.action==='replace'
        ? {replaceImage:{imageObjectId:a.objectId,url,imageReplaceMethod:'CENTER_CROP'}}
        : {createImage:{objectId:a.objectId,url,elementProperties:{pageObjectId:a.pageObjectId,size:a.size,transform:a.transform}}};
      await send([request],cached?undefined:path);
      if(!cached) {
        current=await api.getPresentation(id);
        if(current.revisionId!==revision) throw Error('Concurrent edit during image upload. Reconcile before continuing.');
        const object=current.slides.flatMap(s=>s.pageElements).find(e=>e.objectId===a.objectId);
        if(!object?.image?.sourceUrl) throw Error('Image upload did not return a reusable source URL.');
        urls.set(a.asset,object.image.sourceUrl); // In-memory only; never persist expiring URLs.
      }
    }
    current=await api.getPresentation(id);
    if(current.revisionId!==revision) throw Error('Concurrent edit before geometry pass.');
    const byId=Object.fromEntries(current.slides.flatMap(s=>s.pageElements).map(e=>[e.objectId,e]));
    const requests=[],order=phase.zOrder.slice();
    for(const g of phase.geometry) {
      const t={...g.transform},size=byId[g.objectId].size;
      const emu=d=>d.magnitude*(d.unit==='PT'?12700:1);
      for(const [axis,keys] of [['width',['scaleX','shearY']],['height',['scaleY','shearX']]]) {
        const ratio=emu(g.size[axis])/emu(size[axis]);
        for(const k of keys)t[k]=(t[k]||0)*ratio;
      }
      if(Object.keys(g.crop||{}).length) {
        // Approved nature crops are axis-aligned. Keep original bytes; clip with native masks.
        if(t.shearX||t.shearY) throw Error('Rotated crop requires a dedicated adapter.');
        const c=g.crop,L=c.leftOffset||0,R=c.rightOffset||0,T=c.topOffset||0,B=c.bottomOffset||0;
        if(Math.abs(R)>1e-5||Math.abs(B)>1e-5)throw Error('This adapter supports the approved top/left nature crops only.');
        const x=t.translateX,y=t.translateY,w=emu(size.width)*t.scaleX,h=emu(size.height)*t.scaleY;
        t.scaleX/=1-L-R;t.scaleY/=1-T-B;
        t.translateX=x-L*w/(1-L-R);t.translateY=y-T*h/(1-T-B);
        const masks=[{name:'top',w:12192000,h:y},{name:'left',w:x,h:6858000}];
        for(const m of masks) {
          const maskId=g.objectId+'_clip_'+m.name;
          requests.push({createShape:{objectId:maskId,shapeType:'RECTANGLE',elementProperties:{pageObjectId:phase.pageObjectId,size:{width:{magnitude:3000000,unit:'EMU'},height:{magnitude:3000000,unit:'EMU'}},transform:{scaleX:m.w/3000000,scaleY:m.h/3000000,unit:'EMU'}}}});
          requests.push({updateShapeProperties:{objectId:maskId,shapeProperties:{shapeBackgroundFill:phase.background,outline:{propertyState:'NOT_RENDERED'}},fields:'shapeBackgroundFill,outline.propertyState'}});
          order.splice(order.indexOf(g.objectId)+1,0,maskId);
        }
      }
      requests.push({updatePageElementTransform:{objectId:g.objectId,applyMode:'ABSOLUTE',transform:t}});
    }
    for(const objectId of order)requests.push({updatePageElementsZOrder:{pageElementObjectIds:[objectId],operation:'BRING_TO_FRONT'}});
    await sendChunks(requests);
    await onProgress({slide:phase.slide,status:'applied'});
  }
  current=await api.getPresentation(id);
  if(current.revisionId!==revision)throw Error('Concurrent edit after application; inspect final deck.');
  return current;
}
