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
    q = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H, border=2)   # H: kod czyta się nawet przy ~30% zasłonięcia
    q.add_data(data); q.make()
    m = q.get_matrix(); n = len(m)
    rects = "".join(f'<rect x="{x}" y="{y}" width="1.02" height="1.02"/>' for y, row in enumerate(m) for x, v in enumerate(row) if v)
    return f'<svg viewBox="0 0 {n} {n}" shape-rendering="crispEdges"><rect width="{n}" height="{n}" fill="#fff"/><g fill="#1d1a4a">{rects}</g></svg>'

CSS = """
@page{size:A4;margin:10mm}
body{margin:0;font-family:"DejaVu Sans",sans-serif;color:#1d1a4a}
.sheet{display:grid;grid-template-columns:repeat(2,92mm);grid-auto-rows:92mm;justify-content:center}
.card{border:0.3mm dashed #bbb;box-sizing:border-box;padding:5mm;display:flex;flex-direction:row;align-items:center;gap:3mm;
  background:linear-gradient(90deg,var(--c) 0 50%,#fff 50%);break-inside:avoid;position:relative;border-radius:4mm}
.side{display:flex;flex-direction:column;align-items:center;justify-content:center;width:38mm}
.tag{position:absolute;top:3mm;left:3.5mm;font-size:8px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:#1d1a4a;opacity:.7}
.pic{font-family:"Noto Color Emoji";font-size:96px;line-height:1;height:40mm;display:flex;align-items:center}
.nm{font-weight:800;font-size:17px;margin-top:1mm;text-align:center;line-height:1.1}
.en{font-size:10px;color:#6b678f;margin-bottom:1mm}
.back{background:#fff;flex-direction:column;justify-content:center;gap:2mm}.back .qr{width:74mm;height:74mm;margin:0}.back .lb{font-size:9px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:#6b678f}
.page{break-after:page}
.qr{width:42mm;height:42mm;flex:none}.qr svg{width:100%;height:100%;display:block}
.info{grid-column:1/-1;padding:6mm 8mm;font-size:13px;line-height:1.5;border:0.3mm dashed #bbb;align-self:start}
.info h2{margin:0 0 3mm;font-size:20px}
"""

def front(d, c, pos=""):
    return f'''<div class="card" style="--c:{c['c']};{pos}"><div class="tag">{d['pl']}</div>
      <div class="side"><div class="pic">{c['e']}</div><div class="nm">{c['pl']}</div><div class="en">{c['en']}</div></div>
      <div class="qr">{qr_svg("S1:" + c['id'])}</div></div>'''

def back(d, c, pos):
    return f'''<div class="card back" style="{pos}"><div class="qr">{qr_svg("S1:" + c['id'])}</div>
      <div class="lb">Sowa · {d['pl']}</div></div>'''

def deck_html(d):
    cards = d["cards"]; pages = []
    for k in range(0, len(cards), 6):
        chunk = cards[k:k+6]
        fr = "".join(front(d, c, f"grid-row:{i//2+1};grid-column:{i%2+1}") for i, c in enumerate(chunk))
        # tył: kolumny w lustrzanym odbiciu, żeby przy druku dwustronnym (obrót po dłuższej krawędzi) trafić na przód
        bk = "".join(back(d, c, f"grid-row:{i//2+1};grid-column:{2-i%2}") for i, c in enumerate(chunk))
        pages.append(f'<div class="sheet page">{fr}</div><div class="sheet page">{bk}</div>')
    story = d.get("story", {}).get("title")
    info = f'''<div class="sheet"><div class="info"><h2>Sowa: {d['pl']} ({len(cards)} kart)</h2>
      Gry w aplikacji: „Pokaż mi…”, „Co to jest?”{f", przygoda „{story}”" if story else ""}.<br><br>
      <b>Druk dwustronny (zalecany):</b> co druga strona to tyły kart z dużym kodem. Drukuj dwustronnie, obrót po dłuższej krawędzi.
      Tył ma duży kod, więc kamera złapie kartę nawet wtedy, gdy dziecko trzyma ją obrazkiem do siebie.<br>
      <b>Bez druku dwustronnego:</b> wydrukuj tylko strony z przodami. Mniejszy kod na przodzie też działa.<br><br>
      Najlepiej na grubszym papierze (200–300 g) albo zalaminowane. Wytnij po przerywanej linii. Karty mają 9×9 cm: dziecko trzyma je za brzegi, a kod jest na środku.
      W grze wybierz talię „{d['pl']}”, postaw telefon przednią kamerą do dziecka, przy dobrym świetle.</div></div>'''
    return f'<!doctype html><html lang="pl"><head><meta charset="utf-8"><title>Sowa {d["pl"]}</title><style>{CSS}</style></head><body>{"".join(pages)}{info}</body></html>'

with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page()
    for d in DECKS:
        pg.set_content(deck_html(d)); pg.wait_for_timeout(300)
        path = os.path.join(OUT, f"sowa-{d['id']}.pdf")
        pg.pdf(path=path, format="A4", print_background=True, margin={"top": "10mm", "bottom": "10mm", "left": "10mm", "right": "10mm"})
        print("PDF:", path)
    b.close()
print("decks.js gotowy")
