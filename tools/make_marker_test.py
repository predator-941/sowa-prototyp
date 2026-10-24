"""Kartka do testu znaczników ArUco (4x4) obok obecnych kodów QR. Uruchom: python3 tools/make_marker_test.py
Znaczniki rysuje ta sama biblioteka, która je czyta w test-znaczniki.html, więc słownik na pewno się zgadza."""
import os, sys
from playwright.sync_api import sync_playwright
sys.path.insert(0, os.path.dirname(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "karty", "test-znaczniki.pdf")
import qrcode

def qr_svg(data):
    q = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H, border=2); q.add_data(data); q.make()
    m = q.get_matrix(); n = len(m)
    r = "".join(f'<rect x="{x}" y="{y}" width="1.02" height="1.02"/>' for y, row in enumerate(m) for x, v in enumerate(row) if v)
    return f'<svg viewBox="0 0 {n} {n}" shape-rendering="crispEdges" style="width:100%;height:100%;display:block"><rect width="{n}" height="{n}" fill="#fff"/><g fill="#000">{r}</g></svg>'

vendor = "".join(open(os.path.join(ROOT, "vendor", "aruco", f)).read() + "\n" for f in ("cv.js", "aruco.js", "aruco_4x4_1000.js", "aruco_5x5_1000.js", "apriltag_36h11.js"))
# (id, rozmiar czarnego kwadratu w mm); całość z białym marginesem = 8/6 tego
MARKERS = [(1, 20), (2, 30), (3, 40), (4, 50)]
QRS = [(40, "S1:krowa"), (64, "S1:krowa")]
CSS = """@page{size:A4;margin:10mm}body{margin:0;font-family:"DejaVu Sans";color:#1d1a4a}
h1{font-size:18px;margin:0 0 2mm}p{font-size:10px;margin:0 0 5mm;color:#555;line-height:1.4}
.row{display:flex;flex-wrap:wrap;gap:8mm;align-items:flex-end;margin-bottom:8mm}
.it{text-align:center;font-size:10px;font-weight:700}.it div{margin:0 auto 2mm}.it svg{width:100%;height:100%;display:block}
.card{width:90mm;height:90mm;border:.3mm dashed #999;border-radius:5mm;background:#CFE3F5;display:flex;align-items:center;justify-content:center;flex-direction:column;gap:3mm;font-size:9px;font-weight:700}
.pg{break-before:page}"""

html = f"""<!doctype html><meta charset="utf-8"><style>{CSS}</style><body>
<h1>Test: nowe znaczniki i obecne kody QR</h1>
<p>Otwórz w telefonie stronę test-znaczniki.html. Pokazuj kamerze każdy element z coraz większej odległości i pod kątem.
Zapisz, do jakiej odległości łapie. Rozmiar podany przy znaczniku to czarny kwadrat.</p>
<div class="row" id="mk"></div>
<div class="pg"></div><h1>Inne rodzaje znaczników i kody QR</h1><div class="row" id="mk2"></div>
<div class="row">{"".join(f'<div class="it"><div style="width:{s}mm;height:{s}mm">{qr_svg(d)}</div>QR {s/10:g} cm (krowa)</div>' for s, d in QRS)}</div>
<div class="pg"></div><h1>Karty na próbę: znacznik na środku tyłu karty 9×9 cm</h1>
<p>Wytnij i daj dziecku, niech pokaże sowie. Sprawdź, czy rączka zasłania znacznik.</p>
<div class="row"><div class="card"><div id="c1"></div>znacznik #5 · 3 cm</div><div class="card"><div id="c2"></div>znacznik #6 · 4 cm</div></div>
<div class="row"><div class="card" style="position:relative;display:block" id="c3"></div><div class="card" style="position:relative;display:block" id="c4"></div></div>
<p>Dolne karty: pięć takich samych znaczników jak piątka na kostce (#11 po 1,7 cm, #12 po 2 cm). Rączka zasłoni jeden czy dwa, reszta dalej działa.</p>
<script>{vendor}</script>
<script>
const D=new AR.Dictionary("ARUCO_4X4_1000"), D5=new AR.Dictionary("ARUCO_5X5_1000"), DA=new AR.Dictionary("APRILTAG_36h11");
const svg=(id,mm,dic=D,cells=6)=>{{ const t=mm*(cells+2)/cells; return `<div style="width:${{t}}mm;height:${{t}}mm">`+dic.generateSVG(id).replace("<svg ",'<svg style="width:100%;height:100%;display:block" shape-rendering="crispEdges" ')+"</div>"; }};
document.getElementById("mk").innerHTML={[list(m) for m in MARKERS]}.map(([id,mm])=>`<div class="it">${{svg(id,mm)}}ArUco 4×4 #${{id}} · ${{mm/10}} cm</div>`).join("");
document.getElementById("mk2").innerHTML=[[7,30,D5,7,"ArUco 5×5 #7 · 3 cm"],[8,30,DA,8,"AprilTag #8 · 3 cm"],[9,40,D5,7,"ArUco 5×5 #9 · 4 cm"],[10,40,DA,8,"AprilTag #10 · 4 cm"]].map(([id,mm,d,c,l])=>`<div class="it">${{svg(id,mm,d,c)}}${{l}}</div>`).join("");
const dice=(id,mm)=>{{ const t=mm*8/6, pos=[[50,50],[22,22],[78,22],[22,78],[78,78]];
  return pos.map(([x,y])=>`<div style="position:absolute;left:calc(${{x}}% - ${{t/2}}mm);top:calc(${{y}}% - ${{t/2}}mm)">${{svg(id,mm)}}</div>`).join(""); }};
document.getElementById("c3").innerHTML=dice(11,17); document.getElementById("c4").innerHTML=dice(12,20);
document.getElementById("c1").innerHTML=svg(5,30); document.getElementById("c2").innerHTML=svg(6,40);
</script></body>"""

with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page()
    pg.set_content(html); pg.wait_for_timeout(300)
    pg.pdf(path=OUT, format="A4", print_background=True, margin={"top": "10mm", "bottom": "10mm", "left": "10mm", "right": "10mm"})
    b.close()
print("PDF:", OUT)
