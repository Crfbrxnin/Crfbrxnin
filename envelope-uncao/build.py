logo=open('uncao_logo.svg').read()
W,H=126,156  # 12x15cm + 3mm sangria
css=f"""
@page{{size:{W}mm {H}mm;margin:0}}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{background:#000}}
body{{font-family:'Inter',sans-serif;color:#fff;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
.page{{width:{W}mm;height:{H}mm;position:relative;overflow:hidden;page-break-after:always;
 background:radial-gradient(120% 80% at 30% 15%,#1c1c1c 0%,#0b0b0b 55%,#050505 100%)}}
.page:last-child{{page-break-after:auto}}
.deco{{position:absolute;inset:0;width:100%;height:100%}}
.safe{{position:absolute;left:3mm;top:3mm;width:120mm;height:150mm}}
.logo svg{{width:100%;height:auto;display:block}}
.f .logo{{position:absolute;left:50%;top:22mm;width:34mm;transform:translateX(-50%)}}
.f h1{{position:absolute;left:0;right:0;top:66mm;text-align:center;font-family:'Inter Display','Inter';font-weight:700;
 font-size:25pt;line-height:1.02;letter-spacing:-0.035em}}
.f h1 .amp{{color:#9a9a9a;font-weight:600}}
.f .verse{{position:absolute;left:50%;bottom:24mm;transform:translateX(-50%);width:92mm;padding:4.2mm 5mm 3.6mm;
 border:0.25mm solid rgba(255,255,255,.38);border-radius:4mm;background:linear-gradient(180deg,rgba(255,255,255,.07),rgba(255,255,255,.02));text-align:center}}
.f .verse p{{font-style:italic;font-size:9.2pt;line-height:1.35;color:#ededed}}
.f .verse span{{display:block;margin-top:2mm;font-size:6pt;letter-spacing:.42em;color:#a8a8a8;font-weight:500}}
.b .logo{{position:absolute;left:50%;top:5mm;width:17mm;transform:translateX(-50%)}}
.box{{position:absolute;border:0.25mm solid rgba(255,255,255,.55);border-radius:3mm;background:rgba(255,255,255,.015)}}
.box .hd{{display:flex;align-items:center;gap:2.2mm;position:absolute;left:3.5mm;top:2.8mm}}
.box .hd svg{{width:4.2mm;height:4.2mm;flex:none}}
.box .hd b{{font-weight:600;font-size:7.4pt;letter-spacing:.08em}}
.box .ln{{position:absolute;left:4mm;right:4mm;border-top:0.18mm solid rgba(255,255,255,.4)}}
.qr{{position:absolute;border:0.25mm dashed rgba(255,255,255,.5);border-radius:2.2mm;display:flex;align-items:center;justify-content:center;
 text-align:center;font-size:5.4pt;letter-spacing:.14em;color:rgba(255,255,255,.55);font-weight:500}}
.sub{{position:absolute;font-size:6pt;letter-spacing:.06em;color:#bdbdbd}}
"""
deco_front="""<svg class="deco" viewBox="0 0 126 156" preserveAspectRatio="none">
<defs><linearGradient id="g1" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".18"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
<linearGradient id="sh" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity=".035"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient></defs>
<polygon points="0,156 60,156 0,95" fill="url(#sh)"/><polygon points="126,0 126,60 72,0" fill="url(#sh)"/>
<path d="M-5,12 C35,22 80,14 135,4" fill="none" stroke="url(#g1)" stroke-width=".22"/>
<path d="M45,165 C62,125 95,105 135,98" fill="none" stroke="url(#g1)" stroke-width=".22"/></svg>"""
deco_back="""<svg class="deco" viewBox="0 0 126 156" preserveAspectRatio="none">
<defs><linearGradient id="fl" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#262626"/><stop offset="1" stop-color="#121212"/></linearGradient>
<linearGradient id="g2" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".22"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient></defs>
<path d="M0,0 H126 V14 L70,27 Q63,28.5 56,27 L0,14 Z" fill="url(#fl)"/>
<path d="M0,14 L56,27 Q63,28.5 70,27 L126,14" fill="none" stroke="url(#g2)" stroke-width=".25"/></svg>"""
I_doc='<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5M9 13h6M9 17h6"/></svg>'
I_bank='<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9.5 12 4l9 5.5M4 20h16M6 10v7M10 10v7M14 10v7M18 10v7"/></svg>'
I_pix='<svg viewBox="0 0 24 24" fill="#fff"><path d="M12 2.2 7.4 6.8a2.6 2.6 0 0 1 1.9.8l2.7 2.7 2.7-2.7a2.6 2.6 0 0 1 1.9-.8L12 2.2Zm-6.4 6.2-3.4 3.4a.3.3 0 0 0 0 .4l3.4 3.4h1.7c.4 0 .8-.2 1.1-.4l2.7-2.7a1.3 1.3 0 0 1 1.8 0l2.7 2.7c.3.3.7.4 1.1.4h1.7l3.4-3.4a.3.3 0 0 0 0-.4l-3.4-3.4h-1.7c-.4 0-.8.2-1.1.4l-2.7 2.7a1.3 1.3 0 0 1-1.8 0L8.4 8.8a1.6 1.6 0 0 0-1.1-.4H5.6Zm1.8 8.8L12 21.8l4.6-4.6a2.6 2.6 0 0 1-1.9-.8L12 13.7l-2.7 2.7a2.6 2.6 0 0 1-1.9.8Z"/></svg>'
I_note='<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M11 4H5a2 2 0 0 0-2 2v13a2 2 0 0 0 2 2h13a2 2 0 0 0 2-2v-6"/><path d="M18.5 2.5a2.1 2.1 0 0 1 3 3L12 15l-4 1 1-4z"/></svg>'
def box(x,y,w,h,icon,title,lines=(),extra='',lr=4):
    ls=''.join(f'<div class="ln" style="top:{l}mm;right:{lr}mm"></div>' for l in lines)
    return f'<div class="box" style="left:{x}mm;top:{y}mm;width:{w}mm;height:{h}mm"><div class="hd">{icon}<b>{title}</b></div>{ls}{extra}</div>'
X,BW=8,104
back=(box(X,31,BW,15,I_doc,'CNPJ',(11,)) +
 box(X,50,BW,26,I_bank,'CONTAS BANCÁRIAS',(11.5,17.5,23)) +
 box(X,80,BW,30,I_pix,'PIX',(15.5,22),
     '<div class="sub" style="left:4mm;top:9.3mm">CHAVE</div><div class="qr" style="right:3.5mm;top:3.5mm;width:23mm;height:23mm">QR CODE<br>PIX</div>',lr=31) +
 box(X,114,BW,28,I_note,'OBSERVAÇÕES',(11.5,17.5,23.5)))
html=f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Envelope Unção</title><style>{css}</style></head><body>
<section class="page f">{deco_front}<div class="safe"><div class="logo">{logo}</div>
<h1>Generosidade <span class="amp">&amp;</span><br>Fidelidade</h1>
<div class="verse"><p>“Honra ao Senhor com os teus bens<br>e com as primícias de toda a tua renda.”</p><span>PROVÉRBIOS 3:9</span></div></div></section>
<section class="page b">{deco_back}<div class="safe"><div class="logo">{logo}</div>{back}</div></section>
</body></html>"""
open('envelope.html','w').write(html)
