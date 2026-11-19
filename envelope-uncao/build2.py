import base64
logo=open('uncao_logo.svg').read()
qr=open('qr-pix-cnpj.svg').read()
def font(fam,w,f): return f"@font-face{{font-family:'{fam}';font-weight:{w};src:url(data:font/woff2;base64,{base64.b64encode(open('fonts/'+f,'rb').read()).decode()}) format('woff2')}}"
fonts=font('Archivo Black',400,'archivo-black-latin-400-normal.woff2')+''.join(font('Montserrat',w,f'montserrat-latin-{w}-normal.woff2') for w in (500,700,800))
W,H=126,156
# starburst: rounded rays
import math
def burst(cx,cy,r_in,r_out,n,wid):
    s=''
    for i in range(n):
        a=math.radians(360/n*i)
        x1,y1=cx+r_in*math.cos(a),cy+r_in*math.sin(a); x2,y2=cx+r_out*math.cos(a),cy+r_out*math.sin(a)
        s+=f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="#fff" stroke-width="{wid}" stroke-linecap="round"/>'
    return s
def coil(x,y,n,rx,ry,gap,sw=.45):
    return ''.join(f'<ellipse cx="{x}" cy="{y+i*gap}" rx="{rx}" ry="{ry}" fill="none" stroke="#fff" stroke-width="{sw}"/>' for i in range(n))
css=fonts+f"""
@page{{size:{W}mm {H}mm;margin:0}}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{background:#000}}
body{{font-family:'Montserrat';color:#fff;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
.page{{width:{W}mm;height:{H}mm;position:relative;overflow:hidden;page-break-after:always;background:#0a0a0a}}
.page:last-child{{page-break-after:auto}}
.deco{{position:absolute;inset:0;width:100%;height:100%}}
.logo svg{{width:100%;height:auto;display:block}}
.f .logo{{position:absolute;left:50%;top:13mm;width:24mm;transform:translateX(-50%)}}
.head{{position:absolute;left:15mm;right:15mm;top:38mm;font-family:'Archivo Black';text-transform:uppercase;line-height:.9;letter-spacing:-.01em}}
.head div{{white-space:nowrap;display:block}}
.head .o{{color:transparent;-webkit-text-stroke:.3mm #fff}}
.b .logo{{position:absolute;left:50%;top:6mm;width:17mm;transform:translateX(-50%)}}
.card{{position:absolute;left:50%;top:30mm;transform:translateX(-50%);width:66mm;background:#f2f2f2;border-radius:5mm;padding:4mm 4.5mm 4.5mm;color:#0a0a0a;text-align:center}}
.card .lb{{font-weight:800;font-size:7.5pt;letter-spacing:.12em}}
.pill{{border-radius:10mm;height:6mm;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:7pt}}
.card .pill{{background:#0a0a0a;color:#fff;margin:1.6mm 0 3mm}} .card .k{{font-weight:800;font-size:11pt;height:7.5mm}} .card .k2{{font-size:7.4pt;margin:1.4mm 0 0}}
.qr{{width:38mm;height:38mm;margin:0 auto}}
.bank{{position:absolute;left:0;right:0;top:108mm;text-align:center}}
.bank .nm{{font-weight:800;font-size:11pt;letter-spacing:.04em}}
.bank .row{{display:flex;gap:2.5mm;justify-content:center;margin-top:2.5mm}}
.bank .pill{{background:#f2f2f2;color:#0a0a0a;width:34mm;justify-content:center;font-weight:500}}
.how{{position:absolute;left:0;right:0;top:128mm;text-align:center}}
.how h3{{font-weight:800;font-size:9pt}}
.how p{{font-weight:500;font-size:6.6pt;line-height:1.45;color:#cfcfcf;margin-top:1.8mm}}
"""
deco_front=f'''<svg class="deco" viewBox="0 0 {W} {H}"></svg>'''
deco_back=f'''<svg class="deco" viewBox="0 0 {W} {H}">
<path d="M0,0 H{W} V12 L{W/2+8},25 Q{W/2},26.8 {W/2-8},25 L0,12 Z" fill="#1c1c1c"/>
<path d="M0,12 L{W/2-8},25 Q{W/2},26.8 {W/2+8},25 L{W},12" fill="none" stroke="#fff" stroke-opacity=".35" stroke-width=".3"/>
</svg>'''
lines=[('Sua',''),('generosidade',''),('é semente','o'),('que Deus',''),('multiplica',''),('e transforma','o'),('vidas!','')]
head=''.join(f'<div class="fit {c}">{t}</div>' for t,c in lines)
JS=r"""
document.fonts.ready.then(()=>{const box=document.querySelector('.head');const W=box.clientWidth;
document.querySelectorAll('.fit').forEach(el=>{el.style.fontSize='20px';el.style.display='inline-block';const w=el.scrollWidth;el.style.fontSize=(20*W/w)+'px';el.style.display='block';});
const els=[...document.querySelectorAll('.fit')];const fs=els.map(e=>parseFloat(e.style.fontSize));const med=[...fs].sort((a,b)=>a-b)[Math.floor(fs.length/2)];
els.forEach((e,i)=>{if(fs[i]>med*1.9)e.style.fontSize=(med*1.9)+'px';});
const maxH=box.parentElement.clientHeight*0.6;const k=Math.min(1,maxH/box.scrollHeight);
els.forEach(e=>{e.style.fontSize=(parseFloat(e.style.fontSize)*k)+'px';});box.style.textAlign='left';
const w2=Math.max(...els.map(e=>{e.style.display='inline-block';const w=e.scrollWidth;e.style.display='block';return w;}));box.style.left=((box.parentElement.clientWidth-w2)/2)+'px';box.style.right='auto';
document.body.dataset.ready=1;});
"""
html=f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Envelope Unção II</title><style>{css}</style></head><body>
<section class="page f">{deco_front}<div class="logo">{logo}</div><div class="head">{head}</div></section>
<section class="page b">{deco_back}<div class="logo">{logo}</div>
<div class="card"><div class="lb">PIX · CNPJ</div><div class="pill k">06.301.833/0001-79</div><div class="qr">{qr}</div>
<div class="lb" style="margin-top:3mm;font-size:6pt">OU PELO E-MAIL · EU FAÇO PARTE</div><div class="pill k2">uncaoeufacoparte@gmail.com</div></div>
<div class="bank"><div class="nm">SICOOB 756</div><div class="row"><div class="pill">Agência: <b>&nbsp;3003</b></div><div class="pill">Conta: <b>&nbsp;225.923-0</b></div></div></div>
<div class="how"><h3>Como contribuir pelo QR Code?</h3><p>Abra o app do seu banco e entre na área Pix.<br>Toque em “Ler QR Code” e aponte a câmera.<br>Confira os dados e confirme sua oferta.</p></div>
</section>
<script>{JS}</script></body></html>"""
open('envelope-v2.html','w').write(html)
