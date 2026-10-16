import json, copy, importlib.util
from pathlib import Path
R=Path(__file__).resolve().parents[2]
C={'khaki':'#DED8B8','olive':'#647855','gray':'#5E5D5A','charcoal':'#1F1E1C','cream':'#F0EDDE','white':'#FFFFFF','ochre':'#C7934A'}
slides=[]
def slide(bg):
 s={'background':C[bg],'layers':[]};slides.append(s);return s
def rect(s,x,y,w,h,fill,alpha=1):s['layers'].append(dict(kind='rect',x=x,y=y,w=w,h=h,fill=C.get(fill,fill),alpha=alpha))
def text(s,t,x,y,w,h,size=20,font='Inter',color='gray',bold=False,leading=1.15,align='left',link=None):
 s['layers'].append(dict(kind='text',text=t,x=x,y=y,w=w,h=h,size=size,font=font,color=C[color],bold=bold,leading=leading,align=align,link=link))
def image(s,asset,x,y,w,h):s['layers'].append(dict(kind='image',asset=asset,x=x,y=y,w=w,h=h))
def logo(s,dark=False):image(s,'glyph-small-khaki-4x.png' if dark else 'glyph-small-gray.png',879.687,29.041,52.199,52.199)
def title(s,t,dark=False):
 text(s,t,64,56,790,50,36,'Sen','white' if dark else 'gray',leading=.9);rect(s,64,114,60,1.5,'ochre');logo(s,dark)
def foot(s,n,dark=False):text(s,str(n),465,503,30,18,10,color='white' if dark else 'gray',align='center')
s=slide('charcoal');image(s,'lockup-stacked-khaki.png',64,48,270,97.3)
text(s,'A shared place\nto begin',64,225,700,110,48,'Sen','white',leading=.9)
rect(s,64,365,60,1.5,'ochre')
text(s,'Public design examples',64,395,740,32,22,color='khaki')
text(s,'Fictional project, people, and figures throughout',64,448,800,28,14,color='khaki')
s=slide('charcoal');image(s,'nature-radial.png',526,127.4,594,611);rect(s,0,0,960,540,'charcoal',.82)
text(s,'A neighborhood\nlearning together',64,50,480,90,36,'Sen','white',leading=.9);rect(s,64,146,60,1.5,'ochre');logo(s,True)
text(s,'A fictional garden project gives\nresidents a place to share skills\nand explore what they can grow.',64,185,455,100,20,color='white',leading=1)
text(s,'Work begins with an open workshop\nand a small planting area.',64,305,455,60,20,color='white',leading=1)
text(s,'Small beginnings,\nroom to grow',64,405,440,72,28,'Sen','khaki',leading=.9);foot(s,2,True)
s=slide('olive');title(s,'Three ways to take part',True)
for x,label,head,body in [(64,'LEARN','Shared\nworkshops','Bring a question.\nTry a new skill.\nLearn from a neighbor.'),(348,'GROW','A garden\nin common','Choose a small plot.\nPlan what to plant.\nShare the harvest.'),(632,'CONNECT','A place\nto gather','Meet around a table.\nListen to local stories.\nMake space for others.')]:
 rect(s,x,168,264,286,'cream');text(s,label,x+20,190,224,22,12,'Sen','olive',True,.9)
 text(s,head,x+20,230,224,62,22,'Sen',leading=.9)
 text(s,body,x+20,324,224,99,16)
foot(s,3,True)
s=slide('khaki');image(s,'glyph-large-green.png',292.25,-60.75,720,720);rect(s,0,0,960,540,'khaki',.62);title(s,'An illustrative annual plan')
for x,label,heading,body in [(64,'EXAMPLE BUDGET','$120,000','A fictional annual allowance\nfor space, materials, and\nshared coordination.'),(490,'EXAMPLE CONTRIBUTION','$15,000','A fictional contribution\ntoward workshops and\nseasonal activities.')]:
 rect(s,x,168,406,267,'olive');text(s,label,x+20,190,366,22,12,'Sen','white',True,.9)
 text(s,heading,x+20,230,366,46,28,'Sen','white',leading=.9)
 text(s,body,x+20,305,366,88,16,color='white')
text(s,'Illustrative figures only; not Earthkind financial information.',64,460,832,25,14,color='gray');foot(s,4)
s=slide('charcoal');image(s,'nature-branching.png',428.9,98.6,610,635);rect(s,0,0,960,540,'charcoal',.81);logo(s,True)
text(s,'A conversation\nstarts here',64,126,480,112,48,'Sen','white',leading=.9);rect(s,64,260.8,50,1.5,'ochre')
text(s,'Bring an idea for a shared place\nand imagine what comes next.',64,285,470,68,22,color='white')
text(s,'Alex River and Sam Reed',64,381,450,30,20,color='khaki')
text(s,'Fictional example contacts',64,419,450,22,14,color='khaki')
rect(s,64,461,340,35,'cream');text(s,'hello@example.org',76,467,316,23,16,color='olive',link='mailto:hello@example.org')
layout={'notice':'Entirely fictional public examples; no client deck content or native identifiers.','canvas':{'width':960,'height':540},'slides':slides}
(R/'earthkind-deck/reference/sample-layout.json').write_text(json.dumps(layout,indent=2)+'\n')
def rgb(h):return dict(zip(['red','green','blue'],[int(h[i:i+2],16)/255 for i in (1,3,5)]))
def dim(n):return {'magnitude':n*12700,'unit':'EMU'}
def fill(h,a=1):return {'solidFill':{'color':{'rgbColor':rgb(h)},'alpha':a}}
ref={'presentationId':'SYNTHETIC_REFERENCE','title':'Earthkind fictional public examples','pageSize':{'width':dim(960),'height':dim(540)},'slides':[]}
for i,s in enumerate(slides,1):
 ns={'objectId':f'sample_slide_{i}','pageProperties':{'pageBackgroundFill':fill(s['background'])},'pageElements':[]};ref['slides'].append(ns)
 for j,l in enumerate(s['layers'],1):
  e={'objectId':f'sample_s{i}_e{j}','size':{'width':dim(l['w']),'height':dim(l['h'])},'transform':{'scaleX':1,'scaleY':1,'shearX':0,'shearY':0,'translateX':l['x']*12700,'translateY':l['y']*12700,'unit':'EMU'}}
  if l['kind']=='image':e['image']={'asset':l['asset']}
  else:
   props={'shapeBackgroundFill':fill(l['fill'],l['alpha']) if l['kind']=='rect' else {'propertyState':'NOT_RENDERED'},'outline':{'propertyState':'NOT_RENDERED'},'contentAlignment':'TOP'}
   e['shape']={'shapeType':'RECTANGLE','shapeProperties':props}
   if l['kind']=='text':
    txt=l['text']+'\n';n=len(txt.encode('utf-16-le'))//2
    st={'weightedFontFamily':{'fontFamily':l['font'],'weight':700 if l['bold'] else 400},'fontSize':{'magnitude':l['size'],'unit':'PT'},'foregroundColor':{'opaqueColor':{'rgbColor':rgb(l['color'])}},'bold':l['bold'],'underline':bool(l['link'])}
    if l['link']:st['link']={'url':l['link']}
    ps={'lineSpacing':l['leading']*100,'spaceAbove':{'magnitude':0,'unit':'PT'},'spaceBelow':{'magnitude':0,'unit':'PT'},'alignment':'CENTER' if l['align']=='center' else 'START'}
    e['shape']['text']={'textElements':[{'endIndex':n,'paragraphMarker':{'style':ps}},{'endIndex':n,'textRun':{'content':txt,'style':st}}]}
  ns['pageElements'].append(e)
base=copy.deepcopy(ref);base['presentationId']='SYNTHETIC_TARGET';base['revisionId']='synthetic-revision-1'
for s in base['slides']:
 for e in s['pageElements']:
  if 'image' not in e:e['transform']['translateX']+=12700*5
expected=copy.deepcopy(ref);expected['presentationId']='SYNTHETIC_TARGET'
for name,data in [('reference/recipe.json',ref),('validation/base-before.json',base),('validation/verified.json',expected)]:
 (R/'earthkind-deck'/name).write_text(json.dumps(data,indent=2)+'\n')
spec=importlib.util.spec_from_file_location('compiler',R/'earthkind-deck/scripts/compile.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
plan=m.compile_plan(ref,base)
(R/'earthkind-deck/validation/plan.json').write_text(json.dumps(plan,indent=2)+'\n')
print('Built five wholly synthetic native examples and offline fixtures.')
