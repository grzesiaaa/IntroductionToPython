t = '''Dziwna historia książki
W styczniu 1999 r. przygotowywałem się do zajęć wprowadzających do programowania w języku
Java. Uczyłem tego trzy razy i byłem sfrustrowany. W przypadku tych zajęć wskaźnik braku zaliczenia był
zbyt wysoki. Nawet wśród studentów, którzy zajęcia zaliczyli, ogólny poziom wyników był za niski.
Jednym z problemów, jakie dostrzegłem, były książki. Były zbyt obszerne i zawierały za dużo niepotrzebnych szczegółów dotyczących języka Java, w niewystarczającym stopniu natomiast pojawiały się
w nich ogólne wytyczne związane z tym, jak programować. Wszyscy studenci padali ofiarą efektu
zapadni: zaczynali z łatwością, stopniowo przechodzili dalej, a następnie w okolicach rozdziału 5.
miało miejsce załamanie. Idąc tą drogą, musieliby przyswoić zbyt wiele nowego materiału w zbyt krótkim czasie. Ja byłbym zmuszony poświęcić resztę semestru na wybieranie materiału do nauczenia.
Dwa tygodnie przed pierwszym dniem zajęć zdecydowałem się na napisanie własnej książki. Moje
cele były następujące:
• Zapewnienie zwięzłości. Lepsze dla studentów będzie przeczytanie 10 stron niż nieprzeczytanie 50
stron.
• Zachowanie ostrożności w zakresie terminologii. Spróbowałem zminimalizować żargon i zdefiniować każdy termin przy jego pierwszym użyciu.
• Stopniowe budowanie. Aby uniknąć efektu zapadni, najtrudniejsze zagadnienia podzieliłem
na serie złożone z niewielkich kroków.
• Skoncentrowanie się na programowaniu, a nie na języku programowania. Uwzględniłem minimalny podzbiór przydatnych elementów języka Java i pominąłem resztę.
Potrzebowałem tytułu, dlatego spontanicznie wybrałem następujący: How to Think Like a Computer Scientist (w jaki sposób rozumować jak informatyk).
Moja pierwsza wersja była niedopracowana, ale się sprawdziła. Studenci przeczytali ją w całości i zrozumieli na tyle, że czas na zajęciach mogłem poświęcić na trudne i interesujące zagadnienia, a oni,
co najważniejsze, mogli ćwiczyć.
Książka została wydana w ramach licencji GNU Free Documentation License, która umożliwia
użytkownikom kopiowanie i modyfikowanie treści książki oraz jej dystrybucję.
12  Przedmowa
To, co miało miejsce później, to ciekawa część. Jeff Elkner, nauczyciel w liceum położonym w stanie
Virginia, przystosował moją książkę do języka Python. Wysłał mi kopię swoich modyfikacji. Dzięki
temu miałem okazję w niezwykły sposób uczyć się języka Python, czytając własną książkę.
Pierwsza edycja książki przewidzianej dla języka Python została wydana w 2001 r. przez moje wydawnictwo Green Tea Press.
W 2003 r. zacząłem prowadzić zajęcia na uczelni Olin College i po raz pierwszy uczyłem języka
Python. Kontrast między tym językiem a językiem Java był niesamowity. Studenci mieli mniejsze
trudności, więcej się uczyli, brali udział w bardziej interesujących projektach i ogólnie rzecz biorąc, dawało im to o wiele więcej satysfakcji.
Od tamtego czasu w dalszym ciągu rozwijałem książkę, usuwając błędy, ulepszając niektóre przykłady i dodając materiał, a zwłaszcza ćwiczenia.
Rezultatem jest niniejsza książka, która obecnie ma mniej okazały tytuł. Oto niektóre zmiany:
• Na końcu każdego rozdziału dodałem podrozdział poświęcony debugowaniu. Prezentuję w nim
ogólne techniki znajdowania i unikania błędów, a także ostrzeżenia dotyczące pułapek w kodzie
Python.
• Dodałem więcej ćwiczeń, które obejmują zarówno krótkie testy znajomości zagadnień, jak i kilka
pokaźnych projektów. Większość ćwiczeń zawiera odnośnik do mojego rozwiązania.
• Dodałem serię analiz przypadku — są to obszerniejsze przykłady z ćwiczeniami, rozwiązaniami i omówieniem.
• Rozszerzyłem omówienie planów projektowania programów oraz podstawowych wzorców
projektowych.
• Dołączyłem dodatki dotyczące debugowania i analizy algorytmów.
W drugim wydaniu książki pojawiły się następujące nowości:
• Treść książki wraz z całym dołączonym kodem zaktualizowano pod kątem języka Python 3.
• Dodałem kilka podrozdziałów i więcej szczegółów dotyczących technologii internetowych,
aby początkującym ułatwić uruchamianie kodu Python w przeglądarce. Oznacza to, że nie musisz
zajmować się instalacją środowiska języka Python, jeśli nie uznasz tego za konieczne.
• W podrozdziale „Moduł turtle” rozdziału 4. zrezygnowałem z własnego pakietu graficznego o nazwie Swampy na rzecz bardziej standardowego modułu turtle języka Python, który jest łatwiejszy
do zainstalowania, a ponadto zapewnia większe możliwości.
• Dodałem nowy rozdział zatytułowany „Przydatne elementy” zawierający wprowadzenie do
kilku dodatkowych elementów języka Python, których wykorzystanie nie jest bezwzględnie
konieczne, ale czasami okazują się one przydatne.
Mam nadzieję, że praca z tą książką sprawi Ci przyjemność, a ponadto ułatwi naukę programowania i rozumowania jak informatyk, przynajmniej odrobinę.
— Allen B. Downey
Olin College
Podziękowania  13
Konwencje zastosowane w książce
W książce zastosowano następujące konwencje typograficzne:
Kursywa
Wskazuje nowe pojęcia, adresy URL, adresy e-mail, nazwy plików oraz ich rozszerzenia.
Pogrubienie
Wskazuje terminy zdefiniowane w słowniku.
Czcionka o stałej szerokości
Konwencja używana w treści akapitów w odniesieniu do takich elementów programu jak nazwy zmiennych lub funkcji, a także w przypadku baz danych, typów danych, zmiennych środowiskowych, instrukcji i słów kluczowych.
Pogrubiona czcionka o stałej szerokości
Służy do wskazania poleceń lub innego tekstu, który powinien zostać dosłownie wpisany przez
użytkownika.
Wykorzystanie przykładów z kodem
Dodatkowy materiał (przykłady z kodem, ćwiczenia itp.) jest dostępny do pobrania pod adresem
ftp://ftp.helion.pl/przyklady/myjep2.zip.
Książka ma na celu ułatwienie Ci realizowania zadań. Ogólnie rzecz biorąc, jeśli przykładowy kod
dołączono do książki, możesz używać go we własnych programach i dokumentacji. Nie musisz
kontaktować się z nami, aby uzyskać zgodę, chyba że wykorzystujesz ponownie znaczną część kodu. Na przykład tworzenie programu, w którym użyto kilku porcji kodu z książki, nie wymaga
zgody. Sprzedaż lub dystrybucja dysku CD-ROM z przykładami z książek wydawnictwa wymaga
zgody. Udzielanie odpowiedzi na pytanie poprzez zacytowanie fragmentu z książki i podanie
przykładowego kodu nie wymaga zgody. Dołączenie znacznej ilości przykładowego kodu z książki w dokumentacji własnego produktu wymaga uzyskania zgody.
Doceniamy podanie informacji o prawach autorskich, lecz nie wymagamy tego. Informacje takie
obejmują zwykle tytuł, autora, wydawcę oraz numer ISBN. Oto przykład: „Myśl w języku Python!
Nauka programowania. Wydanie II, Allen B. Downey, Helion, ISBN: 978-83-283-3002-3”.
Jeśli uznasz, że zamierzasz wykorzystać przykłady z kodem w sposób wykraczający poza granice
dozwolonego użycia lub podanych powyżej wariantów uzyskiwania zgody, skontaktuj się z nami
za pośrednictwem adresu helion@helion.pl.
Podziękowania
Gorące podziękowania dla Jeffa Elknera, który przystosował do języka Python moją książkę poświęconą językowi Java. Dzięki temu projekt ten się rozpoczął i nauczyłem się czegoś, co okazało
się później moim ulubionym językiem.
14  Przedmowa
Podziękowania również dla Chrisa Meyersa, który wziął udział w tworzeniu kilku podrozdziałów
książki How to Think Like a Computer Scientist.
Dziękuję organizacji Free Software Foundation za opracowanie licencji GNU Free Documentation License, która ułatwiła mi nawiązanie współpracy z Jeffem i Chrisem. Dziękuję organizacji
Creative Commons za licencję, z której korzystam obecnie.
Dziękuję redaktorom wydawnictwa Lulu, którzy zajmowali się książką How to Think Like a Computer Scientist.
Podziękowania dla redaktorów wydawnictwa O’Reilly Media, którzy pracowali nad książką Think
Python.
Dziękuję wszystkim studentom, którzy brali udział w tworzeniu wcześniejszych wersji książki, oraz
wszystkim współpracownikom (wymienionym poniżej), którzy przesyłali poprawki i sugestie.'''

for znak in set(t):
    if "a" <= znak <= "z":
        ile = t.count(znak)
        print(znak, ile)
        x = ('*'*(int(ile/10)))
        print(x)
