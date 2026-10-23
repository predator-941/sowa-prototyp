"""Szablon nakładki-sowy na telefon (A4, wymiary w mm). Uruchom: python3 tools/make_overlay.py
Mała głowa sowy z jednym okiem-otworem 10 mm. Nakładasz ją gumką na plecy telefonu i przesuwasz,
aż otwór trafi na aparat, więc pasuje do każdego modelu."""
import os
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "karty", "sowa-nakladka.pdf")

def owl(cx, cy, s=1.0, label=True):
    """Głowa sowy wokół (cx, cy). Prawe oko (patrząc na sowę) ma otwór 10 mm na aparat."""
    S = lambda v: v * s
    ex, ey, er = S(15), S(-6), S(13)          # oczy
    hole = 5                                   # promień otworu: zawsze 10 mm średnicy
    head = (f"M{cx-S(36)},{cy+S(10)} C{cx-S(38)},{cy-S(22)} {cx-S(30)},{cy-S(34)} {cx-S(26)},{cy-S(44)} "
            f"L{cx-S(14)},{cy-S(33)} C{cx-S(5)},{cy-S(36)} {cx+S(5)},{cy-S(36)} {cx+S(14)},{cy-S(33)} "
            f"L{cx+S(26)},{cy-S(44)} C{cx+S(30)},{cy-S(34)} {cx+S(38)},{cy-S(22)} {cx+S(36)},{cy+S(10)} "
            f"C{cx+S(33)},{cy+S(36)} {cx+S(14)},{cy+S(42)} {cx},{cy+S(42)} "
            f"C{cx-S(14)},{cy+S(42)} {cx-S(33)},{cy+S(36)} {cx-S(36)},{cy+S(10)} Z")
    # nacięcia na gumkę po bokach (V, 4 mm)
    return f'''
<path d="{head}" fill="#B07A4F" stroke="#1d1a4a" stroke-width="0.5"/>
<path d="M{cx-S(36)},{cy+S(10)} l4,-2.5 l-4,-2.5" fill="#fff" stroke="#1d1a4a" stroke-width="0.5"/>
<path d="M{cx+S(36)},{cy+S(10)} l-4,-2.5 l4,-2.5" fill="#fff" stroke="#1d1a4a" stroke-width="0.5"/>
<ellipse cx="{cx}" cy="{cy+S(6)}" rx="{S(29)}" ry="{S(30)}" fill="#E9C9A0"/>
<circle cx="{cx-ex}" cy="{cy+ey}" r="{er}" fill="#FFF8E6"/>
<circle cx="{cx+ex}" cy="{cy+ey}" r="{er}" fill="#FFF8E6"/>
<circle cx="{cx-ex}" cy="{cy+ey+1}" r="{hole}" fill="#1d1a4a"/>
<circle cx="{cx-ex+1.8}" cy="{cy+ey-1}" r="1.3" fill="#fff"/>
<circle cx="{cx+ex}" cy="{cy+ey}" r="{hole}" fill="#fff" stroke="#1d1a4a" stroke-width="0.5"/>
<circle cx="{cx+ex}" cy="{cy+ey}" r="{hole+1.2}" fill="none" stroke="#EF9F27" stroke-width="1"/>
<path d="M{cx-4},{cy+S(10)} L{cx+4},{cy+S(10)} L{cx},{cy+S(18)} Z" fill="#EF9F27"/>
<path d="M{cx-12},{cy+S(27)} q3 3 6 0 q3 3 6 0 q3 3 6 0 q3 3 6 0" stroke="#C99A6B" stroke-width="0.9" fill="none" stroke-linecap="round"/>
''' + (f'<text x="{cx+ex}" y="{cy+ey+S(21)}" font-size="2.6" text-anchor="middle" fill="#1d1a4a" font-family="DejaVu Sans">wytnij Ø 1 cm</text>' if label else "")

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="210mm" height="297mm" viewBox="0 0 210 297">
<rect width="210" height="297" fill="#fff"/>
<g font-family="DejaVu Sans" fill="#1d1a4a">
<text x="20" y="24" font-size="6" font-weight="bold">Sowa na telefon</text>
<text x="20" y="31" font-size="3.4" fill="#555">Sowa chowa telefon, a jej oko to okienko dla aparatu.</text>
</g>
{owl(70, 95, 1.0)}
{owl(150, 95, 1.0)}
<g font-family="DejaVu Sans" fill="#1d1a4a">
<text x="110" y="155" font-size="2.8" text-anchor="middle" fill="#555">Dwie sowy na kartce: jedna zapasowa albo dla drugiego telefonu.</text>
<text x="20" y="175" font-size="4" font-weight="bold">Jak założyć</text>
<text font-size="3.2">
<tspan x="20" y="184">1. Wydrukuj na grubym papierze albo naklej na tekturę.</tspan>
<tspan x="20" dy="7">2. Wytnij sowę po linii i wytnij otwór w oku (ok. 1 cm), np. dziurkaczem.</tspan>
<tspan x="20" dy="7">3. Przyłóż sowę do pleców telefonu i przesuń ją tak, żeby aparat był widoczny w oku.</tspan>
<tspan x="26" dy="5">Przy kilku obiektywach wybierz główny (zwykle największy).</tspan>
<tspan x="20" dy="7">4. Załóż gumkę recepturkę w nacięcia po bokach, dookoła sowy i telefonu.</tspan>
<tspan x="20" dy="7">5. Postaw telefon pionowo, ekranem do siebie (stojak, książki, kubek).</tspan>
<tspan x="20" dy="7">6. W grze kliknij „Kamera”, żeby włączyć tylną kamerę. Sowa patrzy na dziecko.</tspan>
</text>
<text x="20" y="246" font-size="3" fill="#555">Gumka trzyma sowę w dowolnym miejscu, więc działa z każdym telefonem, także w etui.</text>
</g>
</svg>'''

html = f'<!doctype html><html><head><meta charset="utf-8"><style>@page{{size:A4;margin:0}}body{{margin:0}}svg{{display:block}}</style></head><body>{svg}</body></html>'
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page()
    pg.set_content(html); pg.wait_for_timeout(200)
    pg.pdf(path=OUT, format="A4", print_background=True, margin={"top": "0", "bottom": "0", "left": "0", "right": "0"})
    b.close()
print("PDF:", OUT)
