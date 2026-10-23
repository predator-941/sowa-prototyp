// Wygenerowane przez tools/make_cards.py z tools/decks.py. Nie edytuj ręcznie.
window.DECKS = [
 {
  "id": "pojazdy",
  "pl": "Pojazdy",
  "en": "Vehicles",
  "askPl": "Gdzie jest {n}?",
  "askEn": "Where is the {n}?",
  "cards": [
   {
    "id": "karetka",
    "e": "🚑",
    "pl": "karetka",
    "en": "ambulance",
    "fpl": "Karetka wiezie chorych do szpitala. I-o, i-o!",
    "fen": "An ambulance takes sick people to the hospital.",
    "snd": "siren",
    "c": "#ff6b6b"
   },
   {
    "id": "straz",
    "e": "🚒",
    "pl": "wóz strażacki",
    "en": "fire truck",
    "fpl": "Strażacy gaszą pożary wodą z węża!",
    "fen": "Firefighters put out fires with water.",
    "snd": "siren",
    "c": "#ff8a3d"
   },
   {
    "id": "policja",
    "e": "🚓",
    "pl": "radiowóz",
    "en": "police car",
    "fpl": "Policjanci pilnują, żeby wszyscy byli bezpieczni.",
    "fen": "The police keep everyone safe.",
    "snd": "police",
    "c": "#4d8dff"
   },
   {
    "id": "autobus",
    "e": "🚌",
    "pl": "autobus",
    "en": "bus",
    "fpl": "Autobusem jedzie dużo ludzi naraz. Bip, bip!",
    "fen": "A bus carries lots of people. Beep beep!",
    "snd": "horn",
    "c": "#ffc93c"
   },
   {
    "id": "traktor",
    "e": "🚜",
    "pl": "traktor",
    "en": "tractor",
    "fpl": "Traktor pracuje na polu u rolnika. Brum, brum!",
    "fen": "A tractor works on the farm.",
    "snd": "engine",
    "c": "#5fd39a"
   },
   {
    "id": "pociag",
    "e": "🚂",
    "pl": "pociąg",
    "en": "train",
    "fpl": "Pociąg jedzie po torach. Ciuch, ciuch!",
    "fen": "A train runs on tracks. Choo choo!",
    "snd": "whistle",
    "c": "#a58cff"
   },
   {
    "id": "samolot",
    "e": "✈️",
    "pl": "samolot",
    "en": "airplane",
    "fpl": "Samolot lata wysoko, nad chmurami.",
    "fen": "An airplane flies high above the clouds.",
    "snd": "whoosh",
    "c": "#4fc3f7"
   },
   {
    "id": "helikopter",
    "e": "🚁",
    "pl": "helikopter",
    "en": "helicopter",
    "fpl": "Helikopter ma wielkie śmigło na górze.",
    "fen": "A helicopter has a big rotor on top.",
    "snd": "chopper",
    "c": "#ff9fc2"
   },
   {
    "id": "statek",
    "e": "🚢",
    "pl": "statek",
    "en": "ship",
    "fpl": "Statek pływa po morzu. Tuuut!",
    "fen": "A ship sails on the sea. Toot!",
    "snd": "ship",
    "c": "#3ec9c0"
   },
   {
    "id": "rakieta",
    "e": "🚀",
    "pl": "rakieta",
    "en": "rocket",
    "fpl": "Rakieta leci aż do kosmosu! Trzy, dwa, jeden, start!",
    "fen": "A rocket flies to space! Three, two, one, lift off!",
    "snd": "whoosh",
    "c": "#b388ff"
   }
  ],
  "story": {
   "title": "Zosia jedzie do babci",
   "intro": "Posłuchaj! Zosia jedzie dziś do babci, która mieszka na wyspie nad morzem. Pomożesz jej tam dojechać?",
   "steps": [
    {
     "ans": [
      "autobus"
     ],
     "ask": "Najpierw trzeba dojechać na dworzec. Czym Zosia pojedzie przez miasto? Takim dużym, z wieloma ludźmi w środku…",
     "hint": "To jest duże, jeździ po mieście i ma dużo okien.",
     "after": "Brawo! Zosia wsiada do autobusu. Bip, bip! Jedziemy na dworzec."
    },
    {
     "ans": [
      "pociag"
     ],
     "ask": "Jesteśmy na dworcu! Tu czeka coś bardzo długiego, co jeździ po torach. Co to?",
     "hint": "Jeździ po torach i robi ciuch, ciuch.",
     "after": "Tak! Zosia wsiada do pociągu. Ciuch, ciuch, jedziemy przez pola!"
    },
    {
     "ans": [
      "traktor"
     ],
     "ask": "Zosia patrzy przez okno. Na polu pracuje rolnik. Czym on jeździ po polu?",
     "hint": "Ma wielkie koła i jeździ po polu.",
     "after": "Zgadza się! Rolnik macha do Zosi z traktora. Brum, brum!"
    },
    {
     "ans": [
      "karetka"
     ],
     "ask": "Ojej! Na peronie pan przewrócił się i boli go noga. Kogo trzeba wezwać, żeby pomóc panu?",
     "hint": "Wiezie chorych do szpitala i robi i-o, i-o.",
     "after": "Bardzo dobrze! Karetka już jedzie. Pan będzie zdrowy. Uff!"
    },
    {
     "ans": [
      "statek"
     ],
     "ask": "Babcia mieszka na wyspie. Trzeba przepłynąć przez morze! Czym Zosia popłynie?",
     "hint": "Pływa po wodzie i robi tuuut!",
     "after": "Tak! Zosia płynie wielkim statkiem. Tuuut! Fale robią chlup, chlup."
    },
    {
     "ans": [
      "helikopter"
     ],
     "ask": "Wyspa już blisko! Nad wyspą lata coś, co ma wielkie śmigło na górze. Co to?",
     "hint": "Ma śmigło na górze i umie latać w miejscu.",
     "after": "Brawo! Helikopter wita Zosię na wyspie. Babcia już macha z brzegu!"
    },
    {
     "ans": [
      "rakieta"
     ],
     "ask": "Wieczorem Zosia i babcia patrzą w gwiazdy. Coś leci wysoko, wysoko, aż do kosmosu! Co to?",
     "hint": "Leci do kosmosu! Trzy, dwa, jeden, start!",
     "after": "Tak! To rakieta. Leci do gwiazd."
    }
   ],
   "end": "Zosia przytula babcię. Dziękuje, że jej pomogłeś! To była wspaniała podróż. Dobranoc!"
  },
  "silly": {
   "karetka": "Karetką? Przecież teraz nikt nie jest chory!",
   "straz": "Wozem strażackim? Nigdzie się nie pali!",
   "policja": "Radiowozem? Policjanci mają teraz ważną pracę!",
   "traktor": "Traktorem? Jechalibyśmy bardzo, bardzo długo!",
   "pociag": "Pociągiem? Tutaj nie ma torów!",
   "rakieta": "Rakietą? Wylądowalibyśmy na Księżycu!"
  }
 },
 {
  "id": "zwierzeta",
  "pl": "Zwierzęta",
  "en": "Animals",
  "askPl": "Gdzie jest {n}?",
  "askEn": "Where is the {n}?",
  "cards": [
   {
    "id": "pies",
    "snd": "dog",
    "e": "🐶",
    "pl": "pies",
    "en": "dog",
    "fpl": "Pies pilnuje domu i robi hau, hau!",
    "fen": "A dog guards the house. Woof woof!",
    "c": "#ffc93c"
   },
   {
    "id": "kot",
    "snd": "cat",
    "e": "🐱",
    "pl": "kot",
    "en": "cat",
    "fpl": "Kot lubi mleko i mruczy: mrrr, miau!",
    "fen": "A cat likes milk and says meow!",
    "c": "#ff9fc2"
   },
   {
    "id": "krowa",
    "snd": "cow",
    "e": "🐮",
    "pl": "krowa",
    "en": "cow",
    "fpl": "Krowa daje mleko i robi muuu!",
    "fen": "A cow gives milk and says moo!",
    "c": "#5fd39a"
   },
   {
    "id": "swinia",
    "snd": "pig",
    "e": "🐷",
    "pl": "świnka",
    "en": "pig",
    "fpl": "Świnka lubi błotko i robi chrum, chrum!",
    "fen": "A pig loves mud. Oink oink!",
    "c": "#ff9fc2"
   },
   {
    "id": "kon",
    "snd": "horse",
    "e": "🐴",
    "pl": "koń",
    "en": "horse",
    "fpl": "Koń szybko biega i robi iii-haha!",
    "fen": "A horse runs fast. Neigh!",
    "c": "#ff8a3d"
   },
   {
    "id": "kura",
    "snd": "hen",
    "e": "🐔",
    "pl": "kura",
    "en": "hen",
    "fpl": "Kura znosi jajka i robi ko, ko, ko!",
    "fen": "A hen lays eggs. Cluck cluck!",
    "c": "#ffc93c"
   },
   {
    "id": "owca",
    "snd": "sheep",
    "e": "🐑",
    "pl": "owca",
    "en": "sheep",
    "fpl": "Owca ma ciepłą wełnę i robi beee!",
    "fen": "A sheep has warm wool. Baa!",
    "c": "#4fc3f7"
   },
   {
    "id": "kaczka",
    "snd": "duck",
    "e": "🦆",
    "pl": "kaczka",
    "en": "duck",
    "fpl": "Kaczka pływa w stawie i robi kwa, kwa!",
    "fen": "A duck swims in the pond. Quack!",
    "c": "#3ec9c0"
   },
   {
    "id": "lew",
    "snd": "lion",
    "e": "🦁",
    "pl": "lew",
    "en": "lion",
    "fpl": "Lew to król zwierząt. Groźnie ryczy: wrrraaau!",
    "fen": "The lion is the king of animals. Roar!",
    "c": "#ff8a3d"
   },
   {
    "id": "slon",
    "snd": "elephant",
    "e": "🐘",
    "pl": "słoń",
    "en": "elephant",
    "fpl": "Słoń ma długą trąbę i wielkie uszy.",
    "fen": "An elephant has a long trunk and big ears.",
    "c": "#a58cff"
   },
   {
    "id": "zyrafa",
    "snd": "munch",
    "e": "🦒",
    "pl": "żyrafa",
    "en": "giraffe",
    "fpl": "Żyrafa ma bardzo długą szyję i je liście z drzew.",
    "fen": "A giraffe has a very long neck.",
    "c": "#ffc93c"
   },
   {
    "id": "malpa",
    "snd": "monkey",
    "e": "🐵",
    "pl": "małpka",
    "en": "monkey",
    "fpl": "Małpka skacze po drzewach i lubi banany!",
    "fen": "A monkey climbs trees and loves bananas!",
    "c": "#b388ff"
   }
  ],
  "story": {
   "title": "Wycieczka na wieś",
   "intro": "Zosia jedzie na wieś do dziadka! Dziadek ma dużo zwierząt. Pomożesz Zosi je odnaleźć?",
   "steps": [
    {
     "ans": [
      "pies"
     ],
     "ask": "Przy bramie ktoś wesoło merda ogonem i szczeka: hau, hau! Kto to?",
     "hint": "Pilnuje domu i robi hau, hau.",
     "after": "To Burek! Pies dziadka liże Zosię po ręce. Hi, hi!"
    },
    {
     "ans": [
      "kura"
     ],
     "ask": "Dziadek mówi: chodź, zbierzemy jajka na śniadanie! Kto znosi jajka?",
     "hint": "Robi ko, ko, ko.",
     "after": "Tak! Kury znoszą jajka. Zosia znalazła trzy!"
    },
    {
     "ans": [
      "krowa"
     ],
     "ask": "Teraz potrzebujemy mleka. Które zwierzę daje mleko i robi muuu?",
     "hint": "Jest duża, ma łaty i robi muuu.",
     "after": "Brawo! Krowa Mućka daje pyszne mleko."
    },
    {
     "ans": [
      "kaczka"
     ],
     "ask": "Przy stawie słychać: kwa, kwa! Kto pływa w stawie?",
     "hint": "Pływa i robi kwa, kwa.",
     "after": "To kaczki! Zosia rzuca im okruszki chleba."
    },
    {
     "ans": [
      "kon"
     ],
     "ask": "Na koniec dziadek proponuje przejażdżkę! Na kim pojedziemy?",
     "hint": "Szybko biega i robi iii-haha.",
     "after": "Iii-haha! Zosia jedzie na koniu, a dziadek trzyma uzdę."
    }
   ],
   "end": "Co za dzień! Zosia poznała wszystkie zwierzęta dziadka. Dziękujemy za pomoc!"
  },
  "silly": {
   "lew": "Lew na wsi u dziadka? To by się kury przestraszyły!",
   "slon": "Słoń na wsi? Nie zmieściłby się do stodoły!",
   "zyrafa": "Żyrafa u dziadka? Zjadłaby mu wszystkie jabłka z drzewa!",
   "malpa": "Małpka na wsi? Ona mieszka w dżungli!"
  }
 },
 {
  "id": "warzywa",
  "pl": "Warzywa i owoce",
  "en": "Fruit & veg",
  "askPl": "Gdzie jest {n}?",
  "askEn": "Where is the {n}?",
  "cards": [
   {
    "id": "pomidor",
    "e": "🍅",
    "pl": "pomidor",
    "en": "tomato",
    "fpl": "Pomidor jest czerwony i soczysty.",
    "fen": "A tomato is red and juicy.",
    "c": "#ff6b6b"
   },
   {
    "id": "marchewka",
    "e": "🥕",
    "pl": "marchewka",
    "en": "carrot",
    "fpl": "Marchewka rośnie w ziemi. Chrup, chrup!",
    "fen": "A carrot grows in the ground. Crunch!",
    "c": "#ff8a3d"
   },
   {
    "id": "ziemniak",
    "e": "🥔",
    "pl": "ziemniak",
    "en": "potato",
    "fpl": "Z ziemniaków robi się frytki i puree.",
    "fen": "We make fries from potatoes.",
    "c": "#ffc93c"
   },
   {
    "id": "cebula",
    "e": "🧅",
    "pl": "cebula",
    "en": "onion",
    "fpl": "Cebula ma warstwy i czasem szczypie w oczy!",
    "fen": "An onion has layers and can make you cry!",
    "c": "#b388ff"
   },
   {
    "id": "ogorek",
    "e": "🥒",
    "pl": "ogórek",
    "en": "cucumber",
    "fpl": "Ogórek jest zielony i chrupiący.",
    "fen": "A cucumber is green and crunchy.",
    "c": "#5fd39a"
   },
   {
    "id": "brokul",
    "e": "🥦",
    "pl": "brokuł",
    "en": "broccoli",
    "fpl": "Brokuł wygląda jak małe drzewko!",
    "fen": "Broccoli looks like a little tree!",
    "c": "#5fd39a"
   },
   {
    "id": "papryka",
    "e": "🫑",
    "pl": "papryka",
    "en": "pepper",
    "fpl": "Papryka bywa zielona, żółta i czerwona.",
    "fen": "Peppers can be green, yellow or red.",
    "c": "#3ec9c0"
   },
   {
    "id": "kukurydza",
    "e": "🌽",
    "pl": "kukurydza",
    "en": "corn",
    "fpl": "Z kukurydzy robi się popcorn! Pyk, pyk!",
    "fen": "Popcorn is made from corn! Pop pop!",
    "c": "#ffc93c"
   },
   {
    "id": "jablko",
    "e": "🍎",
    "pl": "jabłko",
    "en": "apple",
    "fpl": "Jabłko rośnie na drzewie w sadzie.",
    "fen": "Apples grow on trees.",
    "c": "#ff6b6b"
   },
   {
    "id": "banan",
    "e": "🍌",
    "pl": "banan",
    "en": "banana",
    "fpl": "Banan ma żółtą skórkę, którą się obiera.",
    "fen": "A banana has a yellow peel.",
    "c": "#ffc93c"
   },
   {
    "id": "truskawka",
    "e": "🍓",
    "pl": "truskawka",
    "en": "strawberry",
    "fpl": "Truskawka jest czerwona i słodka jak cukierek.",
    "fen": "A strawberry is red and sweet.",
    "c": "#ff9fc2"
   },
   {
    "id": "gruszka",
    "e": "🍐",
    "pl": "gruszka",
    "en": "pear",
    "fpl": "Gruszka jest słodka i bardzo soczysta.",
    "fen": "A pear is sweet and juicy.",
    "c": "#5fd39a"
   }
  ],
  "story": {
   "title": "Zupa pomidorowa babci",
   "intro": "Babcia chce ugotować zupę pomidorową, ale ma pustą lodówkę! Pomożesz jej zrobić zakupy na targu?",
   "steps": [
    {
     "ans": [
      "pomidor"
     ],
     "ask": "Najważniejsze do zupy pomidorowej są… no właśnie! Co jest czerwone i okrągłe?",
     "hint": "Od niego zupa ma swoją nazwę.",
     "after": "Brawo! Pomidory lądują w koszyku babci."
    },
    {
     "ans": [
      "marchewka"
     ],
     "ask": "Teraz coś pomarańczowego, co rośnie w ziemi i robi chrup, chrup!",
     "hint": "Lubią ją króliki.",
     "after": "Tak! Marchewka do zupy. Będzie słodka i zdrowa."
    },
    {
     "ans": [
      "cebula"
     ],
     "ask": "Babcia mówi: potrzebuję jeszcze czegoś, od czego czasem płaczą oczy!",
     "hint": "Ma dużo warstw i szczypie w oczy.",
     "after": "Zgadza się, cebula! Babcia ociera łezkę i się śmieje."
    },
    {
     "ans": [
      "ziemniak"
     ],
     "ask": "Na drugie danie będą ziemniaczki z koperkiem. Znajdź ziemniaka!",
     "hint": "Robi się z niego frytki.",
     "after": "Mamy ziemniaki! Zakupy prawie gotowe."
    },
    {
     "ans": [
      "truskawka"
     ],
     "ask": "A na deser… coś czerwonego, słodkiego i małego!",
     "hint": "Rośnie w ogródku latem i jest słodka.",
     "after": "Mmm, truskawki na deser! Babcia jest bardzo zadowolona."
    }
   ],
   "end": "Zupa bulgocze w garnku i pięknie pachnie. Babcia mówi: dziękuję, mój mały kucharzu! Smacznego!"
  },
  "silly": {
   "banan": "Banan w zupie pomidorowej? Fuj! Ha, ha!",
   "jablko": "Jabłko do zupy? To byłaby dziwna zupa!",
   "gruszka": "Gruszka do zupy? Nie, nie!",
   "ogorek": "Ogórek? Babcia zrobi z niego mizerię, ale nie do zupy!",
   "brokul": "Brokuł? Pyszny, ale nie do tej zupy!",
   "kukurydza": "Kukurydza? Zostawmy ją na popcorn!",
   "truskawka": "Truskawki zostawimy na deser!"
  }
 },
 {
  "id": "wieczor",
  "pl": "Wieczór",
  "en": "Bedtime",
  "askPl": "Pokaż mi: {n}!",
  "askEn": "Show me: {n}!",
  "cards": [
   {
    "id": "kolacja",
    "e": "🍽️",
    "pl": "kolacja",
    "en": "dinner",
    "fpl": "Kolacja to ostatni posiłek przed snem.",
    "fen": "Dinner is the last meal before bed.",
    "c": "#ffc93c"
   },
   {
    "id": "kapiel",
    "e": "🛁",
    "pl": "kąpiel",
    "en": "bath",
    "fpl": "W kąpieli zmywamy cały dzień. Chlup, chlup!",
    "fen": "A bath washes the whole day away.",
    "c": "#4fc3f7"
   },
   {
    "id": "pizama",
    "e": "👚",
    "pl": "piżama",
    "en": "pajamas",
    "fpl": "Piżama jest mięciutka i ciepła.",
    "fen": "Pajamas are soft and cosy.",
    "c": "#ff9fc2"
   },
   {
    "id": "zeby",
    "e": "🪥",
    "pl": "mycie zębów",
    "en": "brushing teeth",
    "fpl": "Myjemy ząbki, żeby były zdrowe i białe.",
    "fen": "We brush our teeth to keep them healthy.",
    "c": "#3ec9c0"
   },
   {
    "id": "siku",
    "e": "🚽",
    "pl": "siku",
    "en": "potty",
    "fpl": "Przed snem robimy siku, żeby spać spokojnie.",
    "fen": "We use the potty before bed.",
    "c": "#a58cff"
   },
   {
    "id": "bajka",
    "e": "📖",
    "pl": "bajka",
    "en": "story",
    "fpl": "Bajka na dobranoc to najlepsza część wieczoru!",
    "fen": "A bedtime story is the best part!",
    "c": "#ff8a3d"
   },
   {
    "id": "buziak",
    "e": "😘",
    "pl": "buziak",
    "en": "goodnight kiss",
    "fpl": "Buziak od mamy i taty na dobranoc.",
    "fen": "A goodnight kiss from mum and dad.",
    "c": "#ff6b6b"
   },
   {
    "id": "spanie",
    "e": "🛏️",
    "pl": "spanie",
    "en": "sleep",
    "fpl": "Śpimy, żeby rano mieć dużo siły.",
    "fen": "We sleep to have energy tomorrow.",
    "c": "#b388ff"
   }
  ],
  "story": {
   "title": "Wieczór z Sową",
   "intro": "Robi się ciemno. Sowa pomoże Ci przygotować się do snu! Po każdym kroku pokaż mi kartę.",
   "steps": [
    {
     "ans": [
      "kolacja"
     ],
     "ask": "Najpierw kolacja! Kiedy zjesz, pokaż mi kartę z kolacją.",
     "hint": "Szukaj karty z talerzem.",
     "after": "Mniam! Brzuszek pełny. Brawo!"
    },
    {
     "ans": [
      "kapiel"
     ],
     "ask": "Teraz kąpiel! Chlup, chlup. Po kąpieli pokaż mi kartę z wanną.",
     "hint": "Szukaj karty z wanną.",
     "after": "Czyściutko i pachnąco! Super!"
    },
    {
     "ans": [
      "pizama"
     ],
     "ask": "Zakładamy piżamę! Pokaż mi ją, kiedy będziesz gotowy.",
     "hint": "Szukaj karty z ubrankiem.",
     "after": "Ale ładna piżama! Mięciutko."
    },
    {
     "ans": [
      "zeby"
     ],
     "ask": "Myjemy ząbki! Góra, dół, góra, dół. Pokaż mi szczoteczkę, kiedy skończysz.",
     "hint": "Szukaj karty ze szczoteczką.",
     "after": "Ząbki lśnią jak gwiazdki! Brawo!"
    },
    {
     "ans": [
      "siku"
     ],
     "ask": "Teraz siku przed snem. Pokaż mi kartę, kiedy wrócisz.",
     "hint": "Szukaj karty z toaletą.",
     "after": "Świetnie! Gotowy do łóżka."
    },
    {
     "ans": [
      "bajka"
     ],
     "ask": "Czas na bajkę! Wybierz książeczkę i pokaż mi kartę z bajką.",
     "hint": "Szukaj karty z książką.",
     "after": "Hu, hu! Uwielbiam bajki. Miłego słuchania!"
    },
    {
     "ans": [
      "buziak"
     ],
     "ask": "A teraz buziak na dobranoc dla mamy i taty! Pokaż mi kartę z buziakiem.",
     "hint": "Szukaj karty z buźką, która daje buziaka.",
     "after": "Cmok! Najsłodszy buziak na świecie."
    },
    {
     "ans": [
      "spanie"
     ],
     "ask": "Na koniec: do łóżeczka! Pokaż mi kartę z łóżkiem.",
     "hint": "Szukaj karty z łóżkiem.",
     "after": "Przykrywamy się kołderką…"
    }
   ],
   "end": "Dobranoc! Sowa też idzie spać. Kolorowych snów! Hu, hu."
  },
  "silly": {
   "default": "Hmm, to jeszcze nie teraz! Najpierw zrobimy coś innego."
  }
 },
 {
  "id": "emocje",
  "pl": "Emocje",
  "en": "Feelings",
  "askPl": "Pokaż mi {n}!",
  "askEn": "Show me {n}!",
  "cards": [
   {
    "id": "radosc",
    "e": "😄",
    "pl": "radość",
    "en": "joy",
    "fpl": "Radość! Kiedy się cieszymy, uśmiechamy się od ucha do ucha.",
    "fen": "Joy! We smile from ear to ear.",
    "c": "#ffc93c"
   },
   {
    "id": "smutek",
    "e": "😢",
    "pl": "smutek",
    "en": "sadness",
    "fpl": "Smutek. Czasem płaczemy. Wtedy pomaga przytulas.",
    "fen": "Sadness. A hug helps when we're sad.",
    "c": "#4fc3f7"
   },
   {
    "id": "zlosc",
    "e": "😠",
    "pl": "złość",
    "en": "anger",
    "fpl": "Złość. Kiedy się złościmy, możemy głęboko oddychać: wdech i wydech.",
    "fen": "Anger. Take a deep breath in and out.",
    "c": "#ff6b6b"
   },
   {
    "id": "strach",
    "e": "😨",
    "pl": "strach",
    "en": "fear",
    "fpl": "Strach. Kiedy się boimy, możemy poprosić mamę albo tatę o pomoc.",
    "fen": "Fear. We can ask mum or dad for help.",
    "c": "#a58cff"
   },
   {
    "id": "zdziwienie",
    "e": "😲",
    "pl": "zdziwienie",
    "en": "surprise",
    "fpl": "Zdziwienie! Robimy wielkie oczy i mówimy: ooo!",
    "fen": "Surprise! Big eyes and a big ooh!",
    "c": "#3ec9c0"
   },
   {
    "id": "wstyd",
    "e": "😳",
    "pl": "wstyd",
    "en": "shyness",
    "fpl": "Wstyd. Policzki robią się czerwone. To też jest w porządku.",
    "fen": "Shyness. Our cheeks turn red. That's okay.",
    "c": "#ff9fc2"
   },
   {
    "id": "zmeczenie",
    "e": "🥱",
    "pl": "zmęczenie",
    "en": "tiredness",
    "fpl": "Zmęczenie. Ziewamy i chce nam się spać.",
    "fen": "Tiredness. We yawn and want to sleep.",
    "c": "#b388ff"
   },
   {
    "id": "milosc",
    "e": "🥰",
    "pl": "miłość",
    "en": "love",
    "fpl": "Miłość. Czujemy ją, kiedy przytulamy bliskich.",
    "fen": "Love. We feel it when we hug the people we love.",
    "c": "#ff8a3d"
   }
  ],
  "story": {
   "title": "Na placu zabaw",
   "intro": "Zosia idzie na plac zabaw. Zobaczymy, co dziś poczuje! Pokazuj buźki, które pasują.",
   "steps": [
    {
     "ans": [
      "radosc"
     ],
     "ask": "Zosia widzi swoją ulubioną zjeżdżalnię! Jak się czuje?",
     "hint": "Uśmiecha się od ucha do ucha.",
     "after": "Tak! Zosia się cieszy. Hura, zjeżdżamy!"
    },
    {
     "ans": [
      "zlosc",
      "smutek"
     ],
     "ask": "Ojej, Kuba zabrał Zosi łopatkę bez pytania! Jak czuje się Zosia?",
     "hint": "Może być zła albo smutna.",
     "after": "Tak, to przykre. Zosia mówi: Kuba, oddaj, proszę. To moja łopatka."
    },
    {
     "ans": [
      "wstyd",
      "smutek"
     ],
     "ask": "Kuba oddaje łopatkę i robi się czerwony. Jak czuje się Kuba?",
     "hint": "Policzki robią się czerwone.",
     "after": "Kubie jest głupio. Mówi: przepraszam, Zosiu."
    },
    {
     "ans": [
      "radosc",
      "milosc"
     ],
     "ask": "Zosia i Kuba budują razem wielki zamek z piasku! Jak się czują?",
     "hint": "Razem jest weselej!",
     "after": "Razem bawi się najlepiej! Zamek jest ogromny!"
    },
    {
     "ans": [
      "strach"
     ],
     "ask": "Nagle głośno zaszczekał duży pies! Jak czuje się Zosia?",
     "hint": "Zosia chowa się za mamę.",
     "after": "Zosia się wystraszyła. Mama ją przytula i mówi: jestem przy tobie. Piesek tylko się wita."
    },
    {
     "ans": [
      "zmeczenie"
     ],
     "ask": "Po całym dniu zabawy Zosia ziewa: aaaa… Jak się czuje?",
     "hint": "Ziewa i chce jej się spać.",
     "after": "Czas wracać do domu i odpocząć."
    }
   ],
   "end": "Każda emocja jest ważna. Dziękuję, że pomogłeś Zosi je nazwać! Hu, hu!"
  },
  "silly": {
   "default": "Hmm, czy na pewno? Przyjrzyj się jeszcze raz."
  }
 }
];
