"""Szablon nakładki-sowy na telefon (A4, wymiary w mm). Uruchom: python3 tools/make_overlay.py"""
import os
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "karty", "sowa-nakladka.pdf")

# Geometria (mm). Pasek: nóżka (45x110) -> grzbiet (45x12, na grubość telefonu) -> przód z sową (95x150)
AX0, AX1, AY0, AY1 = 57.5, 152.5, 132, 282      # przód
LX0, LX1 = 82.5, 127.5                           # nóżka i grzbiet
LY0, FOLD1, FOLD2 = 10, 120, 132                 # góra nóżki, zgięcia
N = 4                                            # głębokość nacięć na gumki
n1, n2 = AY0 + 25, AY1 - 25                      # wysokość nacięć

cut = (f"M{LX0},{LY0} L{LX1},{LY0} L{LX1},{AY0} L{AX1},{AY0} "
       f"L{AX1},{n1-3} L{AX1-N},{n1} L{AX1},{n1+3} L{AX1},{n2-3} L{AX1-N},{n2} L{AX1},{n2+3} L{AX1},{AY1} "
       f"L{AX0},{AY1} L{AX0},{n2+3} L{AX0+N},{n2} L{AX0},{n2-3} L{AX0},{n1+3} L{AX0+N},{n1} L{AX0},{n1-3} "
       f"L{AX0},{AY0} L{LX0},{AY0} Z")

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="210mm" height="297mm" viewBox="0 0 210 297">
<rect x="0" y="0" width="210" height="297" fill="#fff"/>
<path d="{cut}" fill="#E9D3B4"/>
<!-- nóżka -->
<text x="105" y="60" font-size="4.2" text-anchor="middle" fill="#8A6A48" font-family="DejaVu Sans">nóżka</text>
<text x="105" y="66" font-size="3" text-anchor="middle" fill="#8A6A48" font-family="DejaVu Sans">(odchyl do tyłu)</text>
<text x="105" y="127.5" font-size="2.6" text-anchor="middle" fill="#8A6A48" font-family="DejaVu Sans">grzbiet: góra telefonu</text>
<!-- sowa -->
<ellipse cx="105" cy="222" rx="40" ry="56" fill="#8A5A3C"/>
<ellipse cx="105" cy="238" rx="26" ry="34" fill="#F2D3A8"/>
<path d="M90 232 q4 4 8 0 q4 4 8 0 q4 4 8 0 M86 244 q5 5 10 0 q5 5 10 0 q5 5 10 0" stroke="#D9A873" stroke-width="1.2" fill="none" stroke-linecap="round"/>
<path d="M66 205 C56 225 58 255 70 262 C68 244 70 222 76 210 Z" fill="#6E4630"/>
<path d="M144 205 C154 225 152 255 140 262 C142 244 140 222 134 210 Z" fill="#6E4630"/>
<path d="M98 180 L112 180 L105 193 Z" fill="#EF9F27"/>
<path d="M92 277 l-3 5 M97 277 v5 M102 277 l3 5 M108 277 l-3 5 M113 277 v5 M118 277 l3 5" stroke="#EF9F27" stroke-width="1.6" stroke-linecap="round"/>
<!-- okulary = okno na aparat (wyciąć) -->
<rect x="62" y="137" width="86" height="38" rx="19" fill="#EF9F27"/>
<rect x="65" y="140" width="80" height="32" rx="16" fill="#fff" stroke="#1d1a4a" stroke-width="0.5"/>
<text x="105" y="153" font-size="3.4" text-anchor="middle" fill="#888" font-family="DejaVu Sans">WYTNIJ</text>
<text x="105" y="158.5" font-size="2.7" text-anchor="middle" fill="#888" font-family="DejaVu Sans">tu patrzy aparat</text>
<!-- linie -->
<path d="{cut}" fill="none" stroke="#1d1a4a" stroke-width="0.5"/>
<line x1="{LX0}" y1="{FOLD1}" x2="{LX1}" y2="{FOLD1}" stroke="#D85A30" stroke-width="0.5" stroke-dasharray="2 1.5"/>
<line x1="{LX0}" y1="{FOLD2}" x2="{LX1}" y2="{FOLD2}" stroke="#D85A30" stroke-width="0.5" stroke-dasharray="2 1.5"/>
<!-- instrukcja (lewa kolumna) -->
<g font-family="DejaVu Sans" fill="#1d1a4a">
<text x="10" y="16" font-size="5" font-weight="bold">Sowa</text>
<text x="10" y="22" font-size="3.2">nakładka na telefon</text>
<text x="10" y="34" font-size="3" font-weight="bold">Jak złożyć</text>
<text font-size="2.7">
<tspan x="10" y="41">1. Wydrukuj na grubym papierze</tspan><tspan x="13" dy="3.6">(200–300 g) albo naklej</tspan><tspan x="13" dy="3.6">na tekturę.</tspan>
<tspan x="10" dy="6">2. Wytnij po ciągłej linii,</tspan><tspan x="13" dy="3.6">także okulary sowy</tspan><tspan x="13" dy="3.6">i nacięcia na gumki.</tspan>
<tspan x="10" dy="6">3. Zegnij po przerywanych</tspan><tspan x="13" dy="3.6">liniach (grzbiet = grubość</tspan><tspan x="13" dy="3.6">telefonu).</tspan>
<tspan x="10" dy="6">4. Przyłóż telefon plecami</tspan><tspan x="13" dy="3.6">do sowy, górą pod grzbiet.</tspan><tspan x="13" dy="3.6">Aparat ma być widoczny</tspan><tspan x="13" dy="3.6">w okularach.</tspan>
<tspan x="10" dy="6">5. Załóż 2 gumki w nacięcia,</tspan><tspan x="13" dy="3.6">dookoła sowy i telefonu.</tspan>
<tspan x="10" dy="6">6. Odchyl nóżkę i postaw.</tspan><tspan x="13" dy="3.6">Ekran patrzy na Ciebie,</tspan><tspan x="13" dy="3.6">sowa na dziecko.</tspan>
<tspan x="10" dy="6">7. W grze kliknij</tspan><tspan x="13" dy="3.6">„Kamera”, żeby włączyć</tspan><tspan x="13" dy="3.6">tylną kamerę.</tspan>
</text>
<line x1="10" y1="152" x2="20" y2="152" stroke="#1d1a4a" stroke-width="0.5"/><text x="22" y="153" font-size="2.6">cięcie</text>
<line x1="10" y1="158" x2="20" y2="158" stroke="#D85A30" stroke-width="0.5" stroke-dasharray="2 1.5"/><text x="22" y="159" font-size="2.6">zgięcie</text>
<text font-size="2.6" fill="#555"><tspan x="10" y="172">Okulary są szerokie,</tspan><tspan x="10" dy="3.6">żeby pasowały do aparatu</tspan><tspan x="10" dy="3.6">w różnych telefonach.</tspan><tspan x="10" dy="3.6">W razie potrzeby przesuń</tspan><tspan x="10" dy="3.6">telefon w bok.</tspan></text>
</g>
</svg>'''

html = f'<!doctype html><html><head><meta charset="utf-8"><style>@page{{size:A4;margin:0}}body{{margin:0}}svg{{display:block}}</style></head><body>{svg}</body></html>'
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page()
    pg.set_content(html); pg.wait_for_timeout(200)
    pg.pdf(path=OUT, format="A4", print_background=True, margin={"top": "0", "bottom": "0", "left": "0", "right": "0"})
    b.close()
print("PDF:", OUT)
