# Sowa i pojazdy: prototyp

Gra dla dzieci: sowa zadaje pytania, dziecko pokazuje wydrukowaną kartę przedniej kamerze telefonu.

## Pliki
- `index.html`: cała gra (jeden plik, bez budowania). Tryby: „Pokaż mi…”, „Co to jest?”, „Przygoda” (Zosia jedzie do babci). Tryb „Bez kamery” pozwala dotykać obrazków.
- `karty.pdf`: 10 kart pojazdów z kodami QR do druku (A4).
- `tools/make_cards.py`: generuje `karty.pdf` (wymaga `pip install qrcode playwright`).

## Kody kart
Każda karta ma kod QR z tekstem `SOWA1:<id>`, np. `SOWA1:karetka`.
Id pojazdów: karetka, straz, policja, autobus, traktor, pociag, samolot, helikopter, statek, rakieta.

## Uruchomienie
Kamera działa tylko pod adresem https, więc grę otwiera się ze strony na Netlify, a nie z pliku na dysku.
Każdy push na gałąź `main` publikuje nową wersję.
