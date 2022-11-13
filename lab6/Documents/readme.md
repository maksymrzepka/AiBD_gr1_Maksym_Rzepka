Maksym Rzepka, 407937

Zbiór danych 12_SWIETOKRZYSKIE.csv
12_SWIETOKRZYSKIE.csv - dane o roznych informacjach dotyczacych zakupow. Mozna wyroznic miedzy innymi informacje o dniach od zakupu danego produktu, marke produktu, wiek kupujacego, plec kupujacego oraz ocene klientow. 
command.ipynb - w tym pliku analizuje ocene ludzi (ze wzgledu na plec) na produkty 5 roznych firm: Beko, Electrolux, Dyson, Tefal i Samsung. Ponad to sprawdzan procentowo ile mezczyzn i kobiet wybiera produkty danej firmy. W analizie uwzgledniam osoby, ktorzy sa klientami wyzej wspomnianych marek lecz nie ma o nich dokladnych danych. Wszystko dokladnie opisuje w pliku command.ipynb na wykresach slupkowych, liniowych oraz kolowych.


1) Original data - folder zawiera oryginalny plik danych oraz metadane.
2) Command files - folder zawierajacy command.ipynb. Szczegolowo opisany powyzej.
3) Analysis Data - folder zawierajacy pliki z danymi   
                dotyczacymi zakupow w wojewodzctwie swietokrzyskim. Wszystkie pliki csv automatycznie zapisaly sie w tym folderze poprzez napisanie odpowiedniego kodu.
4) Documents - folder zawierajacy plik tekstowy readme oraz zrzuty ekranu wykresow.

Opis oryginal data:
- Nazwy kolumn są tworzone w następujący sposób:
    dni od zakupow - ile dni uplynelo od daty zakupu 
                     produktu

- wiek:
    wiek kupujacego

- marka:
    tefal
    samsung
    beko
    dyson
    electrolux

- płeć:
    f = kobieta
    m = mężczyzna
    
- ocena:
    ocena produktu w skali 0-5