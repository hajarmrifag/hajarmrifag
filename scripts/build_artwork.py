"""Generate original, self-contained GitHub SVGs. Python standard library only."""
from pathlib import Path
from html import escape
OUT=Path(__file__).resolve().parents[1]/'assets'
PALETTES={'dark':('#15171c','#f3eee4','#d9bc88','#b8b3a9','#34363b','#202228'),'light':('#f4f0e7','#24262b','#796038','#62615d','#d6cfc2','#eae4d9')}
def text(x,y,value,size,fill,family='sans',**attrs):
 fonts={'sans':'Arial, Helvetica, sans-serif','serif':'Georgia, Times New Roman, serif','mono':'monospace'}
 props=' '.join(f'{k.replace("_","-")}="{escape(str(v))}"' for k,v in attrs.items())
 return f'<text x="{x}" y="{y}" font-family="{fonts[family]}" font-size="{size}" fill="{fill}" {props}>{escape(value)}</text>'
def rect(x,y,w,h,fill,**attrs):
 props=' '.join(f'{k.replace("_","-")}="{v}"' for k,v in attrs.items())
 return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" {props}/>'
def line(x1,y1,x2,y2,color):return f'<path d="M{x1} {y1}L{x2} {y2}" stroke="{color}"/>'
def save(name,w,h,body,title,desc):
 (OUT/name).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc"><title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>'+''.join(body)+'</svg>\n')
def header(theme,mobile):
 bg,ink,brass,muted,rule,panel=PALETTES[theme];w,h=(400,444) if mobile else (960,372);p=28 if mobile else 42
 a=[rect(0,0,w,h,bg),rect(0,0,5,h,brass),text(p,38,'HAJAR MRIFAG / SELECTED WORK',12,muted,'mono',letter_spacing=1.2),line(p,55,w-p,55,rule)]
 if mobile:
  a += [text(p,137,'Hajar',76,ink,'serif'),text(p,216,'Mrifag.',76,ink,'serif'),text(p,264,'AI, systems & product engineering',19,ink),text(p,301,'Sichuan University',16,muted),text(p,326,'Software Engineering · June 2027',16,muted),line(p,359,w-p,359,rule),text(p,393,'MODELS / KERNELS / INTERFACES',13,brass,'mono'),text(p,419,'Chengdu, China',13,muted,'mono')]
  for r in range(5):
   for c in range(5):a.append(rect(298+c*13,88+r*13,9,9,brass if r==c else rule))
 else:
  a += [text(p,151,'Hajar Mrifag.',83,ink,'serif',letter_spacing=-3),text(p,202,'AI, systems & product engineering',27,ink),text(p,247,'Final-year Software Engineering · Sichuan University',17,muted),text(p,276,'Graduating June 2027 · Chengdu, China',17,muted),line(p,308,w-p,308,rule),text(p,340,'MODELS / KERNELS / INTERFACES',14,brass,'mono',letter_spacing=1),text(w-p,340,'ENGINEERING PORTFOLIO',12,muted,'mono',text_anchor='end')]
  for k in range(3):
   x,y=730+k*22,95+k*23;a.append(f'<path d="M{x} {y}l115 -20v118l-115 20Z" fill="{panel}" stroke="{rule}"/>')
  for r in range(5):
   for c in range(5):
    x,y=786+c*18,156+r*18-c*3;a.append(f'<path d="M{x} {y}l12 -2v12l-12 2Z" fill="{brass if r==c or r==2 else rule}"/>')
  a += [line(722,273,915,273,brass),text(725,293,'REASON / BUILD / TEST',11,muted,'mono')]
 save(f'header{"-mobile" if mobile else ""}-{theme}.svg',w,h,a,'Hajar Mrifag — AI, systems and product engineering','Final-year Software Engineering at Sichuan University. Graduating June 2027. Chengdu, China. Abstract tiled artwork references GPU computation; it is not a benchmark plot.')
def evidence_mobile(theme):
 bg,ink,brass,muted,rule,panel=PALETTES[theme]
 a=[rect(0,0,400,458,bg)]
 rows=[('GPU COMPUTING','1.28 TFLOPS','T4 · FP32 GEMM · 1024 × 1024','24% of cuBLAS · kernel time only'),('AI EVALUATION','24 / 31 passed','PolicyLens · 0/3 partial evidence','Synthetic corpus · not held out'),('ALGORITHMS','60,000 commands','Java Order Book · reference checks','40 seeds × 1,500 commands')]
 for i,(label,metric,context,limit) in enumerate(rows):
  y=i*152
  if i:a.append(line(24,y,376,y,rule))
  a += [text(24,y+28,label,14,brass,'mono'),text(24,y+71,metric,34,ink,'serif'),text(24,y+104,context,18,ink),text(24,y+131,limit,17,muted)]
 save(f'evidence-mobile-{theme}.svg',400,458,a,'Engineering evidence snapshots','Recorded CUDA throughput, synthetic PolicyLens evaluation, and finite Java reference-model regression checks. Full context appears in the project descriptions.')

def evidence(theme,mobile):
 if mobile:return evidence_mobile(theme)
 bg,ink,brass,muted,rule,panel=PALETTES[theme];w,h=(480,662) if mobile else (960,254);a=[rect(0,0,w,h,bg)]
 pos=[(28,0),(28,222),(28,444)] if mobile else [(28,0),(346,0),(665,0)]
 for i,(x,y) in enumerate(pos):
  if i:a.append(line(28,y-1,452,y-1,rule) if mobile else line(x-20,26,x-20,228,rule))
 x,y=pos[0];a += [text(x,y+34,'GPU COMPUTING',12,brass,'mono'),text(x,y+76,'1.28 TFLOPS',32,ink,'serif'),text(x,y+103,'FP32 GEMM · Tesla T4 · 1024²',14,muted)]
 for j,(label,v) in enumerate([('Naive',385.648),('Custom',1278.508),('cuBLAS',5322.721)]):a += [text(x,y+133+j*24,label,12,muted,'mono'),rect(x+76,y+123+j*24,190*v/5322.721,12,brass if j==1 else rule)]
 a += [text(x,y+211,'24% of cuBLAS · kernel time only',12,muted)]
 x,y=pos[1];a += [text(x,y+34,'AI EVALUATION',12,brass,'mono'),text(x,y+76,'24 / 31 passed',32,ink,'serif'),text(x,y+103,'PolicyLens · recorded evaluation',14,muted)]
 for i in range(31):a.append(rect(x+(i%16)*17,y+122+(i//16)*22,11,14,brass if i<24 else 'none',stroke=brass if i<24 else muted))
 a += [text(x,y+183,'0 / 3 partial-evidence cases passed',13,ink),text(x,y+211,'Synthetic corpus · not held out',12,muted)]
 x,y=pos[2];a += [text(x,y+34,'ALGORITHMS',12,brass,'mono'),text(x,y+76,'60,000 commands',30,ink,'serif'),text(x,y+103,'Java Order Book · reference checks',14,muted)]
 for i,label in enumerate(['INPUT','BOOK','CHECK']):
  cx=x+i*92;a += [rect(cx,y+129,76,35,panel,stroke=rule),text(cx+38,y+151,label,11,ink,'mono',text_anchor='middle')]
  if i<2:a.append(line(cx+77,y+146,cx+91,y+146,brass))
 a += [text(x,y+187,'40 fixed seeds × 1,500 commands',13,ink),text(x,y+211,'Finite regression set · not a proof',12,muted)]
 save(f'evidence{"-mobile" if mobile else ""}-{theme}.svg',w,h,a,'Three engineering evidence snapshots','Historical T4 GEMM: 1.28 TFLOPS, 24% of cuBLAS, kernel time only. PolicyLens: 24 of 31 pass, 0 of 3 partial-evidence cases pass, synthetic corpus without held-out calibration. Java Order Book: 60,000 generated commands, 40 fixed seeds, finite regression coverage.')
if __name__=='__main__':
 OUT.mkdir(exist_ok=True)
 for theme in PALETTES:
  for mobile in (False,True):header(theme,mobile);evidence(theme,mobile)
