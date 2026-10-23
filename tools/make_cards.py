import qrcode, qrcode.image.svg, io, re
from playwright.sync_api import sync_playwright

V = [("karetka","🚑","karetka","ambulance","#ff6b6b"),("straz","🚒","wóz strażacki","fire truck","#ff8a3d"),
     ("policja","🚓","radiowóz","police car","#4d8dff"),("autobus","🚌","autobus","bus","#ffc93c"),
     ("traktor","🚜","traktor","tractor","#5fd39a"),("pociag","🚂","pociąg","train","#a58cff"),
     ("samolot","✈️","samolot","airplane","#4fc3f7"),("helikopter","🚁","helikopter","helicopter","#ff9fc2"),
     ("statek","🚢","statek","ship","#3ec9c0"),("rakieta","🚀","rakieta","rocket","#b388ff")]

def qr_svg(data):
    q = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, border=2, box_size=10)
    q.add_data(data); q.make()
    m = q.get_matrix(); n = len(m)
    rects = "".join(f'<rect x="{x}" y="{y}" width="1.02" height="1.02"/>' for y,row in enumerate(m) for x,v in enumerate(row) if v)
    return f'<svg viewBox="0 0 {n} {n}" shape-rendering="crispEdges"><rect width="{n}" height="{n}" fill="#fff"/><g fill="#1d1a4a">{rects}</g></svg>'

cards = "".join(f'''<div class="card" style="--c:{c}">
  <div class="pic">{e}</div>
  <div class="nm">{pl}</div><div class="en">{en}</div>
  <div class="qr">{qr_svg("SOWA1:"+i)}</div></div>''' for i,e,pl,en,c in V)

html = f'''<!doctype html><html lang="pl"><head><meta charset="utf-8"><title>Karty Sowa Pojazdy</title>
<style>
@page{{size:A4;margin:10mm}}
body{{margin:0;font-family:"Baloo 2","Nunito","DejaVu Sans",sans-serif;color:#1d1a4a}}
.sheet{{display:grid;grid-template-columns:repeat(3,63mm);grid-auto-rows:88mm;gap:0;justify-content:center}}
.card{{border:0.3mm dashed #bbb;box-sizing:border-box;padding:4mm;display:flex;flex-direction:column;align-items:center;
  background:linear-gradient(var(--c) 0 46%, #fff 46%);break-inside:avoid;position:relative}}
.pic{{font-family:"Noto Color Emoji";font-size:84px;line-height:1;margin-top:4mm;height:36mm;display:flex;align-items:center}}
.nm{{font-weight:800;font-size:19px;margin-top:3mm;text-align:center}}
.en{{font-size:11px;color:#6b678f;margin-bottom:2mm}}
.qr{{width:31mm;height:31mm;margin-top:auto}} .qr svg{{width:100%;height:100%;display:block}}
.info{{grid-column:2/4;padding:6mm 8mm;font-size:13px;line-height:1.5;border:0.3mm dashed #bbb}}
.info h2{{margin:0 0 3mm;font-size:20px}}
</style></head><body>
<div class="sheet">{cards}
<div class="info"><h2>Sowa i pojazdy: karty do gry</h2>
<b>1.</b> Wydrukuj na grubszym papierze (najlepiej 200–300 g) albo zalaminuj.<br>
<b>2.</b> Wytnij karty po przerywanej linii.<br>
<b>3.</b> Otwórz grę, postaw telefon na stole przednią kamerą do dziecka.<br>
<b>4.</b> Sowa pyta „Gdzie jest karetka?”, dziecko pokazuje kartę kamerze.<br><br>
Kod QR musi być dobrze widoczny i niezasłonięty palcami. Najlepiej działa przy dobrym świetle, z odległości 20–40 cm.</div>
</div></body></html>'''
open("karty.html","w").write(html)
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(); pg.set_content(html); pg.wait_for_timeout(500)
    pg.pdf(path="Sowa_pojazdy_karty.pdf", format="A4", print_background=True, margin={"top":"10mm","bottom":"10mm","left":"10mm","right":"10mm"})
    pg.screenshot(path="/tmp/claude-0/-home-claude/792eca66-2980-55e4-851f-98ea98628cee/scratchpad/cards.png", full_page=True)
    b.close()
print("ok")
