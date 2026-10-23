"""Szablon sowy-pacynki (A4, mm). Sowa zakrywa ekran telefonu; przez otwory widać oczy i dziób z gry.
Między uszami jest wcięcie na przednią kamerę. Uruchom: python3 tools/make_puppet.py"""
import os
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "karty", "sowa-pacynka.pdf")

W, H = 82, 168                 # sowa: trochę większa niż typowy telefon
X0, Y0 = 115, 18               # lewy górny róg sowy na kartce
cx = X0 + W / 2
gap, gapd = 46, 15             # wcięcie na kamerę między uszami: szerokość, głębokość
ey, er = Y0 + 46, 10           # oczy: wysokość środka, promień otworu (Ø 20 mm)
ex = 14                        # odstęp oka od środka
by = Y0 + 70                   # dziób
n1, n2 = Y0 + 34, Y0 + H - 34  # nacięcia na gumki

outline = (f"M{X0},{Y0} L{cx-gap/2},{Y0+gapd*0.2} Q{cx-gap/2+4},{Y0+gapd} {cx},{Y0+gapd} "
           f"Q{cx+gap/2-4},{Y0+gapd} {cx+gap/2},{Y0+gapd*0.2} L{X0+W},{Y0} "
           f"L{X0+W},{n1-3} L{X0+W-4},{n1} L{X0+W},{n1+3} L{X0+W},{n2-3} L{X0+W-4},{n2} L{X0+W},{n2+3} "
           f"L{X0+W},{Y0+H-12} Q{X0+W},{Y0+H} {X0+W-12},{Y0+H} L{X0+12},{Y0+H} Q{X0},{Y0+H} {X0},{Y0+H-12} "
           f"L{X0},{n2+3} L{X0+4},{n2} L{X0},{n2-3} L{X0},{n1+3} L{X0+4},{n1} L{X0},{n1-3} Z")
beak = f"M{cx-11},{by-7} L{cx+11},{by-7} L{cx},{by+9} Z"

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="210mm" height="297mm" viewBox="0 0 210 297">
<rect width="210" height="297" fill="#fff"/>
<path d="{outline}" fill="#A9744B"/>
<ellipse cx="{cx}" cy="{Y0+120}" rx="30" ry="38" fill="#E9C9A0"/>
<path d="M{cx-18},{Y0+108} q4.5 4 9 0 q4.5 4 9 0 q4.5 4 9 0 q4.5 4 9 0 M{cx-21},{Y0+122} q5 4.5 10.5 0 q5 4.5 10.5 0 q5 4.5 10.5 0 q5 4.5 10.5 0 M{cx-18},{Y0+136} q4.5 4 9 0 q4.5 4 9 0 q4.5 4 9 0 q4.5 4 9 0" stroke="#C99A6B" stroke-width="1" fill="none" stroke-linecap="round"/>
<path d="M{X0+3},{Y0+92} C{X0-2},{Y0+120} {X0+4},{Y0+150} {X0+16},{Y0+156} C{X0+12},{Y0+135} {X0+12},{Y0+110} {X0+18},{Y0+96} Z" fill="#7E5136"/>
<path d="M{X0+W-3},{Y0+92} C{X0+W+2},{Y0+120} {X0+W-4},{Y0+150} {X0+W-16},{Y0+156} C{X0+W-12},{Y0+135} {X0+W-12},{Y0+110} {X0+W-18},{Y0+96} Z" fill="#7E5136"/>
<path d="M{cx-14},{Y0+H-4} l-3 5 M{cx-9},{Y0+H-4} v5 M{cx-4},{Y0+H-4} l3 5 M{cx+4},{Y0+H-4} l-3 5 M{cx+9},{Y0+H-4} v5 M{cx+14},{Y0+H-4} l3 5" stroke="#EF9F27" stroke-width="1.6" stroke-linecap="round"/>
<!-- obwódki oczu i dzioba -->
<circle cx="{cx-ex}" cy="{ey}" r="{er+3}" fill="#E9C9A0"/><circle cx="{cx+ex}" cy="{ey}" r="{er+3}" fill="#E9C9A0"/>
<!-- otwory do wycięcia -->
<circle cx="{cx-ex}" cy="{ey}" r="{er}" fill="#fff" stroke="#1d1a4a" stroke-width="0.5"/>
<circle cx="{cx+ex}" cy="{ey}" r="{er}" fill="#fff" stroke="#1d1a4a" stroke-width="0.5"/>
<path d="{beak}" fill="#fff" stroke="#1d1a4a" stroke-width="0.5" stroke-linejoin="round"/>
<path d="{outline}" fill="none" stroke="#1d1a4a" stroke-width="0.5"/>
<g font-family="DejaVu Sans" fill="#1d1a4a" text-anchor="middle">
<text x="{cx}" y="{Y0+gapd+6}" font-size="2.6" fill="#fff">tu patrzy kamera</text>
<text x="{cx-ex}" y="{ey+1}" font-size="2.4" fill="#999">wytnij</text>
<text x="{cx+ex}" y="{ey+1}" font-size="2.4" fill="#999">wytnij</text>
</g>
<!-- instrukcja -->
<g font-family="DejaVu Sans" fill="#1d1a4a">
<text x="12" y="26" font-size="6" font-weight="bold">Sowa-pacynka</text>
<text font-size="3"><tspan x="12" y="34">Sowa zasłania ekran.</tspan><tspan x="12" dy="4.2">Przez otwory widać oczy</tspan><tspan x="12" dy="4.2">i dziób, które ruszają się</tspan><tspan x="12" dy="4.2">w grze.</tspan></text>
<text x="12" y="62" font-size="3.6" font-weight="bold">Jak złożyć</text>
<text font-size="2.9">
<tspan x="12" y="70">1. Wydrukuj na grubym papierze</tspan><tspan x="16" dy="4">albo naklej na tekturę.</tspan>
<tspan x="12" dy="6.5">2. Wytnij sowę po linii, oba oczy</tspan><tspan x="16" dy="4">i trójkątny dziób.</tspan>
<tspan x="12" dy="6.5">3. Załóż sowę na ekran telefonu.</tspan><tspan x="16" dy="4">Przednia kamera ma być</tspan><tspan x="16" dy="4">w wcięciu między uszami.</tspan>
<tspan x="12" dy="6.5">4. Przytrzymaj gumkami</tspan><tspan x="16" dy="4">w nacięciach po bokach.</tspan>
<tspan x="12" dy="6.5">5. W grze włącz „Sowa-pacynka”</tspan><tspan x="16" dy="4">i „Kalibruj”. Przesuń palcem</tspan><tspan x="16" dy="4">oczy i dziób pod otwory,</tspan><tspan x="16" dy="4">potem stuknij 2× w dziób.</tspan>
<tspan x="12" dy="6.5">6. Postaw telefon i graj.</tspan><tspan x="16" dy="4">Żeby wyjść: przytrzymaj palec</tspan><tspan x="16" dy="4">w oku sowy przez 2 sekundy.</tspan>
</text>
<text font-size="2.7" fill="#555"><tspan x="12" y="160">Kalibrację robisz raz na telefon,</tspan><tspan x="12" dy="3.8">gra ją zapamięta.</tspan>
<tspan x="12" dy="6">Jeśli gra mówi, że kamera jest</tspan><tspan x="12" dy="3.8">zasłonięta, przesuń sowę</tspan><tspan x="12" dy="3.8">trochę w bok.</tspan></text>
</g>
</svg>'''

html = f'<!doctype html><html><head><meta charset="utf-8"><style>@page{{size:A4;margin:0}}body{{margin:0}}svg{{display:block}}</style></head><body>{svg}</body></html>'
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page()
    pg.set_content(html); pg.wait_for_timeout(200)
    pg.pdf(path=OUT, format="A4", print_background=True, margin={"top": "0", "bottom": "0", "left": "0", "right": "0"})
    b.close()
print("PDF:", OUT)
