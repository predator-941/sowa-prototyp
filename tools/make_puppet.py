"""Szablon sowy-pacynki w kilku rozmiarach (A4, mm), jeden plik PDF.
Sowa zakrywa ekran telefonu; przez otwory widać oczy i dziób z gry. Dół sowy ma być równo z dołem telefonu,
żeby telefon (a nie tektura) opierał się o stojak. Uruchom: python3 tools/make_puppet.py"""
import os
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "karty", "sowa-pacynka.pdf")

# rozmiar: (szerokość, wysokość sowy w mm, dla jakich telefonów, wysokość telefonu w etui)
SIZES = [
    ("S", 68, 137, "małe telefony: iPhone SE, iPhone 12/13 mini", "do ok. 139 mm"),
    ("M", 76, 152, "iPhone 12–17 i Pro, Samsung Galaxy S (zwykły), Google Pixel (zwykły)", "ok. 145–155 mm"),
    ("L", 82, 166, "iPhone Plus i Pro Max, Galaxy S Ultra i S+, Galaxy A, Redmi, Pixel Pro XL", "ok. 157–168 mm"),
]
FONT = 'font-family="DejaVu Sans"'


def owl(W, H, X0=118, Y0=20):
    """Sowa W×H mm, lewy górny róg (X0, Y0). Otwory oczu i dzioba zawsze w tym samym miejscu od góry
    (blisko kamery), reszta sowy skaluje się z rozmiarem."""
    cx = X0 + W / 2
    k, kw = H / 168, W / 82
    gap, gapd = min(46, W - 30), 15     # wcięcie na kamerę między uszami
    ey, er, ex = Y0 + 46, 10, 14        # oczy: Ø 20 mm, ±14 mm od środka
    by = Y0 + 70                        # dziób
    n1, n2 = Y0 + 34, Y0 + H - 34       # nacięcia na gumki
    yb = Y0 + H                         # dół = dół telefonu
    outline = (f"M{X0},{Y0} L{cx-gap/2},{Y0+gapd*0.2} Q{cx-gap/2+4},{Y0+gapd} {cx},{Y0+gapd} "
               f"Q{cx+gap/2-4},{Y0+gapd} {cx+gap/2},{Y0+gapd*0.2} L{X0+W},{Y0} "
               f"L{X0+W},{n1-3} L{X0+W-4},{n1} L{X0+W},{n1+3} L{X0+W},{n2-3} L{X0+W-4},{n2} L{X0+W},{n2+3} "
               f"L{X0+W},{yb-10} Q{X0+W},{yb} {X0+W-10},{yb} L{X0+10},{yb} Q{X0},{yb} {X0},{yb-10} "
               f"L{X0},{n2+3} L{X0+4},{n2} L{X0},{n2-3} L{X0},{n1+3} L{X0+4},{n1} L{X0},{n1-3} Z")
    beak = f"M{cx-11},{by-7} L{cx+11},{by-7} L{cx},{by+9} Z"
    bcy = by + 14 + (yb - 16 - by - 14) / 2          # brzuszek między dziobem a nóżkami
    brx, bry = 29 * kw, (yb - 16 - by - 14) / 2
    feathers = "".join(
        f'<path d="M{cx-16*kw},{bcy+dy} q4 3.5 8 0 q4 3.5 8 0 q4 3.5 8 0 q4 3.5 8 0" stroke="#C99A6B" stroke-width="1" fill="none" stroke-linecap="round" transform="translate({16*kw-16},0)"/>'
        for dy in (-bry * 0.45, -bry * 0.05, bry * 0.35))
    wy1, wy2 = by + 18, yb - 14
    wings = (f'<path d="M{X0+3},{wy1} C{X0-2},{wy1+(wy2-wy1)*.45} {X0+4},{wy2-6} {X0+15},{wy2} C{X0+11},{wy2-20} {X0+11},{wy1+20} {X0+17},{wy1+4} Z" fill="#7E5136"/>'
             f'<path d="M{X0+W-3},{wy1} C{X0+W+2},{wy1+(wy2-wy1)*.45} {X0+W-4},{wy2-6} {X0+W-15},{wy2} C{X0+W-11},{wy2-20} {X0+W-11},{wy1+20} {X0+W-17},{wy1+4} Z" fill="#7E5136"/>')
    feet = f'<path d="M{cx-13},{yb-11} l-3 5 M{cx-8},{yb-11} v5 M{cx-3},{yb-11} l3 5 M{cx+3},{yb-11} l-3 5 M{cx+8},{yb-11} v5 M{cx+13},{yb-11} l3 5" stroke="#EF9F27" stroke-width="1.6" stroke-linecap="round"/>'
    # linie dopasowania na dole i linia docięcia ucha przy kamerze w rogu
    trims = (f'<path d="M{X0+2},{yb-3} H{X0+W-2} M{X0+2},{yb-6} H{X0+W-2}" stroke="#fff" stroke-width="0.35" stroke-dasharray="1.5 1.2"/>'
             f'<text x="{X0+W+2}" y="{yb-2.2}" font-size="2.3" {FONT} fill="#555">−3 mm</text>'
             f'<text x="{X0+W+2}" y="{yb-5.6}" font-size="2.3" {FONT} fill="#555">−6 mm</text>'
             f'<path d="M{X0+3},{Y0+16} L{X0+16},{Y0+3}" stroke="#fff" stroke-width="0.35" stroke-dasharray="1.5 1.2"/>'
             f'<path d="M{X0+W-3},{Y0+16} L{X0+W-16},{Y0+3}" stroke="#fff" stroke-width="0.35" stroke-dasharray="1.5 1.2"/>')
    return f'''
<path d="{outline}" fill="#A9744B"/>
<ellipse cx="{cx}" cy="{bcy}" rx="{brx}" ry="{bry}" fill="#E9C9A0"/>
{feathers}{wings}{feet}
<circle cx="{cx-ex}" cy="{ey}" r="{er+3}" fill="#E9C9A0"/><circle cx="{cx+ex}" cy="{ey}" r="{er+3}" fill="#E9C9A0"/>
<circle cx="{cx-ex}" cy="{ey}" r="{er}" fill="#fff" stroke="#1d1a4a" stroke-width="0.5"/>
<circle cx="{cx+ex}" cy="{ey}" r="{er}" fill="#fff" stroke="#1d1a4a" stroke-width="0.5"/>
<path d="{beak}" fill="#fff" stroke="#1d1a4a" stroke-width="0.5" stroke-linejoin="round"/>
{trims}
<path d="{outline}" fill="none" stroke="#1d1a4a" stroke-width="0.5"/>
<g {FONT} text-anchor="middle">
<text x="{cx}" y="{Y0+gapd+6}" font-size="2.6" fill="#fff">tu patrzy kamera</text>
<text x="{cx-ex}" y="{ey+1}" font-size="2.4" fill="#999">wytnij</text>
<text x="{cx+ex}" y="{ey+1}" font-size="2.4" fill="#999">wytnij</text>
</g>
<path d="M{X0-6},{yb} H{X0+W+6}" stroke="#d33" stroke-width="0.4"/>
<text x="{cx}" y="{yb+5}" font-size="2.8" {FONT} fill="#d33" text-anchor="middle">dół sowy = dół telefonu</text>'''


def ruler(x, y):
    ticks = "".join(f'<path d="M{x+i*10},{y} v{-3 if i % 5 else -5}" stroke="#1d1a4a" stroke-width="0.3"/>' for i in range(11))
    return (f'<path d="M{x},{y} H{x+100}" stroke="#1d1a4a" stroke-width="0.4"/>{ticks}'
            f'<text x="{x}" y="{y+4.5}" font-size="2.6" {FONT} fill="#555">Ta linia ma dokładnie 10 cm. Jeśli jest krótsza, drukuj w skali 100%.</text>')


def page(name, W, H, phones, ph_h):
    svg_owl = owl(W, H, X0=194 - W)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="210mm" height="297mm" viewBox="0 0 210 297">
<rect width="210" height="297" fill="#fff"/>
{svg_owl}
<g {FONT} fill="#1d1a4a">
<text x="12" y="26" font-size="6" font-weight="bold">Sowa-pacynka · {name}</text>
<text x="12" y="33" font-size="3.2" fill="#555">{W}×{H} mm · telefon w etui {ph_h}</text>
<foreignObject x="12" y="36" width="98" height="20"><div xmlns="http://www.w3.org/1999/xhtml" style="font:2.9px DejaVu Sans;color:#1d1a4a;line-height:1.35">{phones}</div></foreignObject>
<text x="12" y="62" font-size="3.6" font-weight="bold">Jak złożyć</text>
<text font-size="2.9">
<tspan x="12" y="70">1. Wydrukuj w skali 100% na grubym</tspan><tspan x="16" dy="4">papierze albo naklej na tekturę.</tspan>
<tspan x="12" dy="6.5">2. Wytnij sowę po linii, oba oczy</tspan><tspan x="16" dy="4">i trójkątny dziób.</tspan>
<tspan x="12" dy="6.5">3. Przyłóż do telefonu: kamera w wcięciu</tspan><tspan x="16" dy="4">między uszami, dół sowy równo</tspan><tspan x="16" dy="4">z dołem telefonu. Jeśli sowa wystaje,</tspan><tspan x="16" dy="4">przytnij dół po linii −3 albo −6 mm.</tspan>
<tspan x="12" dy="6.5">4. Kamera w rogu ekranu? Dotnij ucho</tspan><tspan x="16" dy="4">po przerywanej linii.</tspan>
<tspan x="12" dy="6.5">5. Przytrzymaj gumkami w nacięciach.</tspan>
<tspan x="12" dy="6.5">6. W grze stuknij „Ustaw sowę”. Sowa</tspan><tspan x="16" dy="4">poprosi: dotknij palcem przez lewe</tspan><tspan x="16" dy="4">oko, prawe oko, a potem dziób.</tspan>
<tspan x="12" dy="6.5">7. Postaw telefon i graj.</tspan><tspan x="16" dy="4">Żeby wyjść: przytrzymaj palec</tspan><tspan x="16" dy="4">w oku sowy przez 2 sekundy.</tspan>
</text>
</g>
{ruler(12, 275)}
</svg>'''


def guide():
    rows = "".join(f'<tr><td><b>{n}</b></td><td>{ph_h}</td><td>{p}</td><td>strona {i+2}</td></tr>' for i, (n, W, H, p, ph_h) in enumerate(SIZES))
    return f'''<div style="width:210mm;height:297mm;box-sizing:border-box;padding:22mm 18mm;font-family:DejaVu Sans;color:#1d1a4a">
<h1 style="font-size:22px;margin:0 0 3mm">Sowa-pacynka: wybierz rozmiar</h1>
<p style="font-size:12px;line-height:1.5;color:#444">Zmierz wysokość telefonu razem z etui (od góry do dołu) i wydrukuj tylko stronę z pasującym rozmiarem.
Dół sowy ma być równo z dołem telefonu, wtedy telefon stoi stabilnie na stojaku, a tektura nie przeszkadza.
Jeśli jesteś pomiędzy rozmiarami, wybierz większy i przytnij dół po linii −3 lub −6 mm.</p>
<table style="border-collapse:collapse;font-size:11.5px;width:100%;margin-top:6mm" cellpadding="8">
<tr style="background:#f3ecdf;text-align:left"><th>Rozmiar</th><th>Telefon w etui</th><th>Przykładowe telefony</th><th>Wydrukuj</th></tr>{rows}</table>
<p style="font-size:11px;color:#666;margin-top:8mm;line-height:1.5">Szerokość nie musi się zgadzać co do milimetra: sowa może być trochę szersza niż telefon.
Przy pierwszej grze sowa poprosi, żeby dotknąć jej oczu i dzioba przez otwory. Wtedy gra wie, gdzie je pokazać, więc pasuje do każdego modelu.</p></div>'''


html = ('<!doctype html><html><head><meta charset="utf-8"><style>@page{size:A4;margin:0}body{margin:0}svg{display:block;break-after:page}</style></head><body>'
        + guide() + "".join(page(*s) for s in SIZES) + "</body></html>")
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page()
    pg.set_content(html); pg.wait_for_timeout(300)
    pg.pdf(path=OUT, format="A4", print_background=True, margin={"top": "0", "bottom": "0", "left": "0", "right": "0"})
    b.close()
print("PDF:", OUT)
