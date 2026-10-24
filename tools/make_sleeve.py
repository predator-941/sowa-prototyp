"""Wykrój sowy-tulei (obwoluty) na telefon, w rozmiarach S, M, L (A4 poziomo, wymiary w mm).
Tuleja otwarta z góry i z dołu: wycinasz, zaginasz, sklejasz z tyłu i wsuwasz telefon.
Dwa zaczepy u góry z tyłu zaginają się na górną krawędź telefonu, więc tuleja wisi na telefonie
i nie zsuwa się na stojak. Przód ma otwory na oczy i dziób z gry oraz wcięcie na przednią kamerę.
Uruchom: python3 tools/make_sleeve.py"""
import os
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "karty", "sowa-tuleja.pdf")
FONT = 'font-family="DejaVu Sans"'

# rozmiar: szerokość przodu W (wnętrze, telefon w etui), wysokość H (trochę mniej niż telefon), grubość boku D
SIZES = [
    ("S", 71, 130, 12, "iPhone SE, iPhone mini (telefon w etui do ok. 70 mm szerokości)"),
    ("M", 77, 144, 12, "iPhone 12–17 i Pro, Galaxy S, Pixel (do ok. 76 mm szerokości)"),
    ("L", 83, 156, 13, "iPhone Plus i Pro Max, Galaxy S Ultra i A, Redmi, Pixel XL (do ok. 82 mm)"),
]
GLUE = 10          # pasek do klejenia
HOOK_W, HOOK_TAB = 14, 7   # zaczep: szerokość i zakładka, która wchodzi na przód telefonu


def sleeve(W, H, D, x0=12, y0=None):
    y0 = y0 if y0 is not None else 12 + D + HOOK_TAB      # góra paneli = góra telefonu
    xs = [x0, x0 + GLUE, x0 + GLUE + W / 2, x0 + GLUE + W / 2 + D, x0 + GLUE + W / 2 + D + W,
          x0 + GLUE + W / 2 + 2 * D + W, x0 + GLUE + W + 2 * D + W]   # granice: klej | tył L | bok | przód | bok | tył P
    g0, bl0, sl0, f0, sr0, br0, end = xs
    yb = y0 + H
    fx, cx = f0, f0 + W / 2
    gap, gapd = min(46, W - 26), 15                      # wcięcie na kamerę między uszami
    ey, er, ex, by = y0 + 46, 10, 14, y0 + 70            # oczy Ø 20 mm, dziób jak w pacynce
    # obrys zewnętrzny (linia cięcia): przód z wcięciem, reszta prosto, zaczepy na tyle przy bokach
    hl = (sl0 - HOOK_W, sl0)          # zaczep na lewej połówce tyłu, przy lewym boku
    hr = (br0, br0 + HOOK_W)          # zaczep na prawej połówce tyłu, przy prawym boku
    top_hook = lambda a, b: f"L{a},{y0} L{a},{y0-D-HOOK_TAB+2} Q{a},{y0-D-HOOK_TAB} {a+2},{y0-D-HOOK_TAB} L{b-2},{y0-D-HOOK_TAB} Q{b},{y0-D-HOOK_TAB} {b},{y0-D-HOOK_TAB+2} L{b},{y0} "
    cut = (f"M{g0},{y0+4} L{bl0},{y0} " + top_hook(*hl) +
           f"L{fx},{y0} L{cx-gap/2},{y0+gapd*0.2} Q{cx-gap/2+4},{y0+gapd} {cx},{y0+gapd} "
           f"Q{cx+gap/2-4},{y0+gapd} {cx+gap/2},{y0+gapd*0.2} L{fx+W},{y0} " + top_hook(*hr) +
           f"L{end},{y0} L{end},{yb} L{bl0},{yb} L{g0},{yb-4} Z")
    folds = "".join(f'<path d="M{x},{y0} V{yb}" />' for x in (bl0, sl0, f0, sr0, br0))
    folds += "".join(f'<path d="M{a},{y0} H{b} M{a},{y0-D} H{b}" />' for a, b in (hl, hr))
    beak = f"M{cx-11},{by-7} L{cx+11},{by-7} L{cx},{by+9} Z"
    bcy, bry = (by + 14 + yb - 14) / 2, (yb - 14 - by - 14) / 2
    feathers = "".join(f'<path d="M{cx-15},{bcy+dy} q3.75 3.5 7.5 0 q3.75 3.5 7.5 0 q3.75 3.5 7.5 0 q3.75 3.5 7.5 0" />'
                       for dy in (-bry * .45, -bry * .05, bry * .35))
    wing = lambda x: (f'<path d="M{x+D/2},{y0+60} C{x+D+3},{y0+80} {x+D+3},{yb-40} {x+D/2},{yb-12} '
                      f'C{x-3},{yb-40} {x-3},{y0+80} {x+D/2},{y0+60} Z" fill="#7E5136"/>')
    back_feathers = "".join(f'<path d="M{x},{y} q4 4 8 0" />' for x0b, x1b in ((bl0, sl0), (br0, end))
                            for y in range(int(y0 + 20), int(yb - 8), 12) for x in range(int(x0b + 4), int(x1b - 8), 10))
    return f'''
<path d="{cut}" fill="#A9744B"/>
<rect x="{g0}" y="{y0}" width="{GLUE}" height="{H}" fill="#e8e1d6"/>
<text x="{g0+GLUE/2}" y="{(y0+yb)/2}" font-size="3" {FONT} fill="#777" text-anchor="middle" transform="rotate(-90 {g0+GLUE/2} {(y0+yb)/2})">klej</text>
<rect x="{sl0}" y="{y0}" width="{D}" height="{H}" fill="#93603C"/><rect x="{sr0}" y="{y0}" width="{D}" height="{H}" fill="#93603C"/>
{wing(sl0)}{wing(sr0)}
<g stroke="#C08A5C" stroke-width="1" fill="none" stroke-linecap="round">{back_feathers}</g>
<ellipse cx="{cx}" cy="{bcy}" rx="{W*0.36}" ry="{bry}" fill="#E9C9A0"/>
<g stroke="#C99A6B" stroke-width="1" fill="none" stroke-linecap="round">{feathers}</g>
<path d="M{cx-13},{yb-11} l-3 5 M{cx-8},{yb-11} v5 M{cx-3},{yb-11} l3 5 M{cx+3},{yb-11} l-3 5 M{cx+8},{yb-11} v5 M{cx+13},{yb-11} l3 5" stroke="#EF9F27" stroke-width="1.6" stroke-linecap="round"/>
<circle cx="{cx-ex}" cy="{ey}" r="{er+3}" fill="#E9C9A0"/><circle cx="{cx+ex}" cy="{ey}" r="{er+3}" fill="#E9C9A0"/>
<circle cx="{cx-ex}" cy="{ey}" r="{er}" fill="#fff" stroke="#1d1a4a" stroke-width="0.5"/>
<circle cx="{cx+ex}" cy="{ey}" r="{er}" fill="#fff" stroke="#1d1a4a" stroke-width="0.5"/>
<path d="{beak}" fill="#fff" stroke="#1d1a4a" stroke-width="0.5" stroke-linejoin="round"/>
<g stroke="#fff" stroke-width="0.4" stroke-dasharray="2 1.5" fill="none">{folds}</g>
<path d="{cut}" fill="none" stroke="#1d1a4a" stroke-width="0.5"/>
<g {FONT} text-anchor="middle" font-size="2.4">
<text x="{cx}" y="{y0+gapd+6}" fill="#fff">tu patrzy kamera</text>
<text x="{cx-ex}" y="{ey+1}" fill="#999">wytnij</text><text x="{cx+ex}" y="{ey+1}" fill="#999">wytnij</text>
<text x="{(bl0+sl0)/2}" y="{yb-4}" fill="#fff">tył</text><text x="{(br0+end)/2}" y="{yb-4}" fill="#fff">tył</text>
<text x="{sum(hl)/2}" y="{y0-D-2}" fill="#fff" font-size="2">zaczep</text><text x="{sum(hr)/2}" y="{y0-D-2}" fill="#fff" font-size="2">zaczep</text>
</g>''', end


def page(name, W, H, D, phones):
    svg, end = sleeve(W, H, D)
    tx = end + 8
    lines = [("Sowa-tuleja · " + name, 6, "bold", 20), (f"przód {W} mm · bok {D} mm · wys. {H} mm", 3, "normal", 27)]
    steps = ["1. Wydrukuj w skali 100%, najlepiej", "    na kartonie 200–250 g.",
             "2. Wytnij po ciągłej linii, oba oczy", "    i trójkątny dziób.",
             "3. Zegnij po wszystkich przerywanych", "    liniach (pomaga tępy nóż i linijka).",
             "4. Posmaruj pasek „klej” i sklej z drugim", "    końcem tyłu. Wyjdzie tuleja.",
             "5. Wsuń telefon ekranem do przodu.", "    Kamera ma być w wcięciu między uszami.",
             "6. Zegnij zaczepy na górną krawędź", "    telefonu. Tuleja wisi na telefonie,", "    a dół telefonu stoi na stojaku.",
             "7. W grze: „Ustaw sowę” i dotknij", "    przez otwory: lewe oko, prawe, dziób."]
    txt = "".join(f'<text x="{tx}" y="{y}" font-size="{s}" font-weight="{w}" {FONT} fill="#1d1a4a">{t}</text>' for t, s, w, y in lines)
    txt += f'<foreignObject x="{tx}" y="30" width="{285-tx}" height="14"><div xmlns="http://www.w3.org/1999/xhtml" style="font:2.7px DejaVu Sans;color:#555;line-height:1.35">{phones}</div></foreignObject>'
    txt += "".join(f'<text x="{tx}" y="{50+i*4.6}" font-size="2.9" {FONT} fill="#1d1a4a" xml:space="preserve">{t}</text>' for i, t in enumerate(steps))
    txt += (f'<text x="{tx}" y="{50+len(steps)*4.6+5}" font-size="2.6" {FONT} fill="#777">Linia ciągła = cięcie, przerywana = zgięcie.</text>'
            f'<text x="{tx}" y="{50+len(steps)*4.6+9}" font-size="2.6" {FONT} fill="#777">Bardzo grube etui? Weź większy rozmiar.</text>')
    rx, ry = 12, 203
    ruler = "".join(f'<path d="M{rx+i*10},{ry} v{-2.5 if i % 5 else -4}" stroke="#1d1a4a" stroke-width="0.3"/>' for i in range(11))
    ruler = (f'<path d="M{rx},{ry} H{rx+100}" stroke="#1d1a4a" stroke-width="0.4"/>{ruler}'
             f'<text x="{rx+104}" y="{ry}" font-size="2.4" {FONT} fill="#555">Ta linia ma dokładnie 10 cm. Jeśli jest krótsza, drukuj w skali 100%.</text>')
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="297mm" height="210mm" viewBox="0 0 297 210"><rect width="297" height="210" fill="#fff"/>{svg}{txt}{ruler}</svg>'


html = ('<!doctype html><html><head><meta charset="utf-8"><style>@page{size:A4 landscape;margin:0}body{margin:0}svg{display:block;break-after:page}</style></head><body>'
        + "".join(page(*s) for s in SIZES) + "</body></html>")
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page()
    pg.set_content(html); pg.wait_for_timeout(300)
    pg.pdf(path=OUT, width="297mm", height="210mm", print_background=True, margin={"top": "0", "bottom": "0", "left": "0", "right": "0"})
    b.close()
print("PDF:", OUT)
