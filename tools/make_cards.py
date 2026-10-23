"""Generuje decks.js (dane dla gry) i PDF-y z kartami do druku dla każdej talii z decks.py.
Uruchom z głównego folderu repo:  python3 tools/make_cards.py
Wymaga: pip install qrcode playwright && playwright install chromium (oraz czcionki Noto Color Emoji dla emoji)."""
import json, os, sys
import qrcode
from playwright.sync_api import sync_playwright

sys.path.insert(0, os.path.dirname(__file__))
from decks import DECKS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "karty")
os.makedirs(OUT, exist_ok=True)

# sprawdź unikalność id
ids = [c["id"] for d in DECKS for c in d["cards"]]
dup = {i for i in ids if ids.count(i) > 1}
assert not dup, f"Powtórzone id kart: {dup}"

with open(os.path.join(ROOT, "decks.js"), "w") as f:
    f.write("// Wygenerowane przez tools/make_cards.py z tools/decks.py. Nie edytuj ręcznie.\n")
    f.write("window.DECKS = " + json.dumps(DECKS, ensure_ascii=False, indent=1) + ";\n")

def qr_svg(data):
    q = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, border=2)
    q.add_data(data); q.make()
    m = q.get_matrix(); n = len(m)
    rects = "".join(f'<rect x="{x}" y="{y}" width="1.02" height="1.02"/>' for y, row in enumerate(m) for x, v in enumerate(row) if v)
    return f'<svg viewBox="0 0 {n} {n}" shape-rendering="crispEdges"><rect width="{n}" height="{n}" fill="#fff"/><g fill="#1d1a4a">{rects}</g></svg>'

CSS = """
@page{size:A4;margin:10mm}
body{margin:0;font-family:"DejaVu Sans",sans-serif;color:#1d1a4a}
.sheet{display:grid;grid-template-columns:repeat(3,63mm);grid-auto-rows:88mm;justify-content:center}
.card{border:0.3mm dashed #bbb;box-sizing:border-box;padding:4mm;display:flex;flex-direction:column;align-items:center;
  background:linear-gradient(var(--c) 0 46%,#fff 46%);break-inside:avoid;position:relative}
.tag{position:absolute;top:3mm;left:3.5mm;font-size:8px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:#1d1a4a;opacity:.7}
.pic{font-family:"Noto Color Emoji";font-size:84px;line-height:1;margin-top:4mm;height:36mm;display:flex;align-items:center}
.nm{font-weight:800;font-size:18px;margin-top:3mm;text-align:center;line-height:1.1}
.en{font-size:11px;color:#6b678f;margin-bottom:2mm}
.qr{width:31mm;height:31mm;margin-top:auto}.qr svg{width:100%;height:100%;display:block}
.info{grid-column:1/-1;padding:6mm 8mm;font-size:13px;line-height:1.5;border:0.3mm dashed #bbb;align-self:start}
.info h2{margin:0 0 3mm;font-size:20px}
"""

def deck_html(d):
    cards = "".join(f'''<div class="card" style="--c:{c['c']}"><div class="tag">{d['pl']}</div>
      <div class="pic">{c['e']}</div><div class="nm">{c['pl']}</div><div class="en">{c['en']}</div>
      <div class="qr">{qr_svg("SOWA1:" + c['id'])}</div></div>''' for c in d["cards"])
    story = d.get("story", {}).get("title")
    info = f'''<div class="info"><h2>Sowa: {d['pl']} ({len(d['cards'])} kart)</h2>
      Gry w aplikacji: „Pokaż mi…”, „Co to jest?”{f", przygoda „{story}”" if story else ""}.<br>
      <b>1.</b> Wydrukuj na grubszym papierze (200–300 g) albo zalaminuj. <b>2.</b> Wytnij po przerywanej linii.
      <b>3.</b> W grze wybierz talię „{d['pl']}”, postaw telefon przednią kamerą do dziecka.<br>
      Kod QR musi być widoczny i niezasłonięty palcami. Najlepiej działa przy dobrym świetle, z 20–40 cm.</div>'''
    return f'<!doctype html><html lang="pl"><head><meta charset="utf-8"><title>Sowa {d["pl"]}</title><style>{CSS}</style></head><body><div class="sheet">{cards}{info}</div></body></html>'

with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page()
    for d in DECKS:
        pg.set_content(deck_html(d)); pg.wait_for_timeout(300)
        path = os.path.join(OUT, f"sowa-{d['id']}.pdf")
        pg.pdf(path=path, format="A4", print_background=True, margin={"top": "10mm", "bottom": "10mm", "left": "10mm", "right": "10mm"})
        print("PDF:", path)
    b.close()
print("decks.js gotowy")
