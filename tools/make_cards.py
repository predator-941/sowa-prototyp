"""Generuje decks.js (dane dla gry) i PDF-y z kartami do druku dla każdej talii z decks.py.
Uruchom z głównego folderu repo:  python3 tools/make_cards.py
Wymaga: pip install qrcode playwright && playwright install chromium (oraz czcionki Noto Color Emoji dla emoji)."""
import base64, json, os, sys
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
.card{border:0.3mm dashed #bbb;box-sizing:border-box;padding:3mm 0;display:flex;flex-direction:column;align-items:center;justify-content:space-between;
  background:var(--c);break-inside:avoid;position:relative;border-radius:5mm}
.top{font-size:9px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;opacity:.65;height:5mm}
.pic{height:64mm;width:76mm;display:flex;align-items:center;justify-content:center}
.pic img{max-width:100%;max-height:100%}
.pic .em{font-family:"Noto Color Emoji";font-size:170px;line-height:1}
.nm{font-weight:800;font-size:18px;height:8mm}.nm small{font-weight:400;font-size:10px;color:#4b4770}
.back{background:#CFE3F5}
.qr{width:64mm;height:64mm;position:relative;border-radius:2mm;overflow:hidden}.qr svg{width:100%;height:100%;display:block}
.owl{position:absolute;left:50%;top:50%;width:13mm;height:13mm;margin:-6.5mm;background:#fff;border-radius:50%;
  font-family:"Noto Color Emoji";font-size:32px;display:flex;align-items:center;justify-content:center}
.g{position:absolute;top:0;bottom:0;width:13mm;display:flex;align-items:center;justify-content:center;font-size:20px;text-align:center;opacity:.55}
.g.l{left:0}.g.r{right:0}.g span{display:block;font-size:6px;line-height:1.2;font-weight:700}
.page{break-after:page}
.info{grid-column:1/-1;padding:6mm 8mm;font-size:13px;line-height:1.5;border:0.3mm dashed #bbb;align-self:start}
.info h2{margin:0 0 3mm;font-size:20px}
"""

IMG = os.path.join(ROOT, "img")

def picture(c):
    """Ostry obrazek SVG z folderu img/ (jeśli jest), inaczej emoji."""
    f = os.path.join(IMG, c["id"] + ".svg")
    if os.path.exists(f):
        data = base64.b64encode(open(f, "rb").read()).decode()
        return f'<img src="data:image/svg+xml;base64,{data}">'
    return f'<div class="em">{c["e"]}</div>'

GRIP = '<div class="g l">✋<span>trzymaj<br>tutaj</span></div><div class="g r">✋<span>trzymaj<br>tutaj</span></div>'

def front(d, c, pos=""):
    # przód: duży obrazek, bez kodu
    return f'''<div class="card" style="--c:{c['c']};{pos}"><div class="top">{d['pl']}</div>
      <div class="pic">{picture(c)}</div><div class="nm">{c['pl'].capitalize()} <small>{c['en']}</small></div></div>'''

def back(d, c, pos):
    # tył: kod na środku, ramka do trzymania po bokach (kod H czyta się nawet z kciukami na brzegach kodu)
    return f'''<div class="card back" style="{pos}">{GRIP}<div class="top">Sowa · {d['pl']}</div>
      <div class="qr">{qr_svg("S1:" + c['id'])}<div class="owl">🦉</div></div><div class="nm"></div></div>'''

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
      Przód karty to obrazek, tył to kod dla sowy. Dziecko patrzy na obrazek, a kod jest zwrócony do kamery.<br>
      <b>Druk dwustronny:</b> obrót po dłuższej krawędzi (co druga strona to tyły).<br>
      <b>Bez druku dwustronnego:</b> wydrukuj wszystko, wytnij i sklej przody z tyłami plecami (ta sama pozycja na kartce, lustrzanie).<br><br>
      Najlepiej na grubszym papierze (200–300 g) albo zalaminowane. Karty mają 9×9 cm. Dziecko trzyma je za ramkę po bokach, kod jest na środku.
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
