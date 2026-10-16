"""Compile native Slides updates for a semantically identical base deck.

Offline only: produces requests; an authenticated Slides client executes them.
Refuses different content rather than overwriting it. General decks use the guide.
"""
import argparse, copy, json, re
from pathlib import Path

def mul(a,b):
    ax,ay,ah,av,at,au=[a.get(k,0) for k in ['scaleX','scaleY','shearX','shearY','translateX','translateY']]
    bx,by,bh,bv,bt,bu=[b.get(k,0) for k in ['scaleX','scaleY','shearX','shearY','translateX','translateY']]
    assert a.get('unit','EMU')=='EMU' and b.get('unit','EMU')=='EMU'
    return dict(scaleX=ax*bx+ah*bv,scaleY=av*bh+ay*by,shearX=ax*bh+ah*by,shearY=av*bx+ay*bv,translateX=ax*bt+ah*bu+at,translateY=av*bt+ay*bu+au,unit='EMU')

def flat(elements,parent=None):
    for source in elements:
        e=copy.deepcopy(source);e['transform']=mul(parent or {'scaleX':1,'scaleY':1},e.get('transform',{}))
        if 'elementGroup' in e:
            yield from flat(e['elementGroup']['children'],e['transform'])
        else: yield e

def text(e):
    return ''.join(t.get('textRun',{}).get('content','') for t in e.get('shape',{}).get('text',{}).get('textElements',[]))

def normalized(s): return re.sub(r'\s+',' ',s).strip()
def utf16(s): return len(s.encode('utf-16-le'))//2
def rng(a,b): return dict(type='FIXED_RANGE',startIndex=a,endIndex=b)

def compile_plan(reference, base):
    assert reference['pageSize']==base['pageSize'], 'Page sizes differ; scale deliberately.'
    assert len(reference['slides'])==len(base['slides']), 'Archetype matching required for different slide counts.'
    phases=[];audit=[]
    for i,(rs,bs) in enumerate(zip(reference['slides'],base['slides']),1):
        ref=list(flat(rs['pageElements']));orig={e['objectId']:e for e in flat(bs['pageElements'])}
        assert not any('elementGroup' in e for e in bs['pageElements']), 'Base has groups; inspect before applying this adapter.'
        active=ref; ids={e['objectId'] for e in active}
        for e in ref:
            if e['objectId'] in orig:
                assert normalized(text(e))==normalized(text(orig[e['objectId']])), f'Content changed: slide {i}, {e["objectId"]}'
        for key,e in orig.items():
            assert key in {e['objectId'] for e in ref} or not normalized(text(e)), f'Unexpected text would be removed: {key}'
        requests=[{'updatePageProperties':{'objectId':bs['objectId'],'pageProperties':{'pageBackgroundFill':rs['pageProperties']['pageBackgroundFill']},'fields':'pageBackgroundFill'}}]
        for key in orig.keys()-ids: requests.append({'deleteObject':{'objectId':key}})
        assets=[]
        for e in active:
            key=e['objectId'];new=key not in orig
            if new:
                if 'shape' in e:
                    requests.append({'createShape':{'objectId':key,'shapeType':e['shape']['shapeType'],'elementProperties':{'pageObjectId':bs['objectId'],'size':e['size'],'transform':e['transform']}}})
                elif 'image' in e:
                    assets.append({'action':'create','objectId':key,'pageObjectId':bs['objectId'],'size':e['size'],'transform':e['transform'],'asset':e['image']['asset']})
                    continue
                else: raise ValueError('Unsupported new object '+key)
            else:
                tr=copy.deepcopy(e['transform'])
                # Native size can differ after image replacement; geometry phase handles it later.
                if 'image' not in e:
                    for axis,keys in [('width',['scaleX','shearY']),('height',['scaleY','shearX'])]:
                        ratio=e['size'][axis]['magnitude']/orig[key]['size'][axis]['magnitude']
                        for k in keys:tr[k]*=ratio
                    requests.append({'updatePageElementTransform':{'objectId':key,'applyMode':'ABSOLUTE','transform':tr}})
            if 'image' in e:
                if e['image'].get('asset'):assets.append({'action':'replace','objectId':key,'asset':e['image']['asset']})
                continue
            if 'line' in e:
                p=e['line']['lineProperties'];requests.append({'updateLineProperties':{'objectId':key,'lineProperties':p,'fields':','.join(p)}});continue
            shape=e['shape'];props=shape.get('shapeProperties',{})
            p={k:copy.deepcopy(props[k]) for k in ['shapeBackgroundFill','outline','contentAlignment'] if k in props}
            p['autofit']={'autofitType':'NONE'}
            requests.append({'updateShapeProperties':{'objectId':key,'shapeProperties':p,'fields':','.join(k if k!='autofit' else 'autofit.autofitType' for k in p)}})
            txt=text(e)
            if not txt:continue
            requests.append({'deleteText':{'objectId':key,'textRange':{'type':'ALL'}}})
            requests.append({'insertText':{'objectId':key,'insertionIndex':0,'text':txt[:-1] if txt.endswith('\n') else txt}})
            requests.append({'deleteParagraphBullets':{'objectId':key,'textRange':{'type':'ALL'}}})
            n=utf16(txt)
            runs=shape['text']['textElements']
            for te in runs:
                if 'paragraphMarker'in te and 'bullet'in te['paragraphMarker']:
                    requests.append({'createParagraphBullets':{'objectId':key,'textRange':rng(te.get('startIndex',0),min(te['endIndex'],n)),'bulletPreset':'BULLET_DISC_CIRCLE_SQUARE'}})
            # ALL includes the terminal paragraph's bullet; a fixed range can miss it.
            first=copy.deepcopy(next(te['textRun']['style'] for te in runs if 'textRun' in te));first.pop('fontFamily',None)
            requests.append({'updateTextStyle':{'objectId':key,'textRange':{'type':'ALL'},'style':first,'fields':','.join(first)}})
            for te in runs:
                a,b=te.get('startIndex',0),min(te['endIndex'],n)
                if b<=a:continue
                if 'textRun'in te:
                    st=copy.deepcopy(te['textRun']['style']);st.pop('fontFamily',None)
                    requests.append({'updateTextStyle':{'objectId':key,'textRange':rng(a,b),'style':st,'fields':','.join(st)+(',link' if 'link'not in st else '')}})
                if 'paragraphMarker'in te:
                    st=te['paragraphMarker']['style'];requests.append({'updateParagraphStyle':{'objectId':key,'textRange':rng(a,b),'style':st,'fields':','.join(st)}})
        phases.append({'slide':i,'pageObjectId':bs['objectId'],'requests':requests,'assets':assets,'geometry':[{'objectId':e['objectId'],'size':e['size'],'transform':e['transform'],'crop':e['image'].get('imageProperties',{}).get('cropProperties',{}) if e['image'].get('asset','').startswith('nature-') else {}} for e in active if 'image'in e],'background':rs['pageProperties']['pageBackgroundFill'],'zOrder':[e['objectId'] for e in active]})
        audit.append({'slide':i,'contentMatch':True,'retainedObjects':len(ids & orig.keys()),'removedObsoleteObjects':sorted(orig.keys()-ids),'addedObjects':sorted(ids-orig.keys()),'styleRequests':len(requests)})
    return {'formatVersion':1,'targetPresentationId':base['presentationId'],'baseRevision':base.get('revisionId'),'phases':phases,'audit':audit}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--reference',required=True);p.add_argument('--base',required=True);p.add_argument('--output',required=True);a=p.parse_args()
    plan=compile_plan(json.loads(Path(a.reference).read_text()),json.loads(Path(a.base).read_text()))
    Path(a.output).write_text(json.dumps(plan,indent=2));print(json.dumps({'slides':len(plan['phases']),'requests':sum(len(x['requests']) for x in plan['phases']),'audit':plan['audit']}))
