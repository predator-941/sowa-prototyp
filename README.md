# Sowa i pojazdy: prototyp

Gra dla dzieci: sowa zadaje pytania, dziecko pokazuje wydrukowaną kartę przedniej kamerze telefonu.

## Pliki
- `index.html`: cała gra (jeden plik, bez budowania). Tryby: „Pokaż mi…”, „Co to jest?”, „Przygoda” (Zosia jedzie do babci). Tryb „Bez kamery” pozwala dotykać obrazków.
- `vendor/`: biblioteka qr-scanner (licencja MIT) do odczytu kodów, działa w tle, nie blokuje gry.
- `decks.js`: dane wszystkich talii dla gry (generowane, nie edytuj ręcznie).
- `karty/`: PDF-y do druku, po jednym na talię (Pojazdy, Zwierzęta, Warzywa i owoce, Wieczór, Emocje), plus `sowa-nakladka.pdf`: tekturowa sowa na telefon, która chowa ekran (generuje ją `tools/make_overlay.py`), oraz `sowa-pacynka.pdf`: sowa zakładana na ekran, z otworami na oczy i dziób z gry (`tools/make_puppet.py`).
- `tools/decks.py`: **tu dodajesz i edytujesz talie**: karty, ciekawostki, przygody, śmieszne odpowiedzi.
- `tools/make_cards.py`: z `decks.py` generuje `decks.js` i PDF-y (wymaga `pip install qrcode playwright`).

## Kody kart
Każda karta ma kod QR z tekstem `SOWA1:<id>`, np. `SOWA1:karetka`.
Id kart są w `tools/decks.py` i muszą być unikalne we wszystkich taliach.

## Uruchomienie
Kamera działa tylko pod adresem https, więc grę otwiera się ze strony na Netlify, a nie z pliku na dysku.
Każdy push na gałąź `main` publikuje nową wersję.
