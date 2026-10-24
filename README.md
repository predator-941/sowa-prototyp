# Sowa i pojazdy: prototyp

Gra dla dzieci: sowa zadaje pytania, dziecko pokazuje wydrukowaną kartę przedniej kamerze telefonu.

## Pliki
- `index.html`: cała gra (jeden plik, bez budowania). Tryby: „Pokaż mi…”, „Co to jest?”, „Przygoda” (Zosia jedzie do babci). Tryb „Bez kamery” pozwala dotykać obrazków.
- `vendor/`: biblioteka qr-scanner (licencja MIT) do odczytu kodów, działa w tle, nie blokuje gry.
- `decks.js`: dane wszystkich talii dla gry (generowane, nie edytuj ręcznie).
- `karty/`: PDF-y do druku, po jednym na talię (Pojazdy, Zwierzęta, Warzywa i owoce, Wieczór, Emocje), plus `sowa-nakladka.pdf`: tekturowa sowa na telefon, która chowa ekran (generuje ją `tools/make_overlay.py`), oraz `sowa-pacynka.pdf`: sowa zakładana na ekran w rozmiarach S, M i L (dół sowy równo z dołem telefonu), z otworami na oczy i dziób z gry (`tools/make_puppet.py`).
- `img/`: ostre obrazki kart (SVG, nazwa = id karty). Jeśli karta ma tu plik, PDF używa go zamiast emoji. Teraz są tu zwierzęta z Noto Emoji (licencja w `img/LICENSE.txt`).
- `tools/decks.py`: **tu dodajesz i edytujesz talie**: karty, ciekawostki, przygody, śmieszne odpowiedzi.
- `tools/make_cards.py`: z `decks.py` generuje `decks.js` i PDF-y (wymaga `pip install qrcode playwright`).

## Test znaczników
`test-znaczniki.html` to osobna strona testowa (nie część gry): kamera porównuje na żywo nowe znaczniki ArUco 4×4 (biblioteka js-aruco2 w `vendor/aruco/`, licencja w środku) z obecnymi kodami QR. Kartkę do druku robi `tools/make_marker_test.py` → `karty/test-znaczniki.pdf`.

## Kody kart
Przód karty to duży obrazek, tył to kod QR na środku z ramką do trzymania. Kod ma tekst `S1:<id>`, np. `S1:karetka` (stare `SOWA1:` też działa).
Id kart są w `tools/decks.py` i muszą być unikalne we wszystkich taliach.

## Jak aplikacja
`manifest.webmanifest`, `sw.js` i `icons/` pozwalają dodać grę do ekranu początkowego: otwiera się wtedy z ikonki sowy, na całym ekranie, bez paska przeglądarki. Na Androidzie gra pokazuje przycisk „Dodaj”, na iPhonie instrukcję (Udostępnij → Do ekranu początkowego).

## Uruchomienie
Kamera działa tylko pod adresem https, więc grę otwiera się ze strony na Netlify, a nie z pliku na dysku.
Każdy push na gałąź `main` publikuje nową wersję.
