Maksym Rzepka, 407937

Zbiór danych tb.csv
tb.csv - dane o gruźlicy w różnych grupach pacjentów (tabela koduje jednocześnie informacje o wieku i o płci w kolumnach i zawiera dużo pustych miejsc)
command.ipynb - w tym pliku analizuje liczbe zachorowan na gruzlice dla wszystkich sasiadow polski wraz z sama polska i       wyswietlam dane na wykresach liczby zachorowan od roku, nastepnie wszystkich chorych na gruzlice ludzi pochodzacych z panstw sasiadujacych z polska porownuje na jednym wspolnym wykresie w celu dokladnego przeanalizowania i porownania danych. Sumuje mezczyzn i kobiety z kazdego przedzialu wiekowego, aby stworzyc wykres przedstawiajacy zachorowania wsrod kobiet i mezczyzn.
Na koncu analizuje wszystkie kobiety oraz mezczyzn zachorowanych na gruzlice zamieszkalych w sasiadujacych panstwach polski.
Wszystkie.

1) Original data - folder zawiera oryginalny plik danych oraz metadane.
2) Command files - folder zawierajacy command.ipynb. Szczegolowo opisany powyzej.
3) Analysis Data - folder zawierajacy pliki z danymi (dane dotycza zachorowan na gruzlice) poszczegolnych panstw.
                   sasiadujacych z polska. Wszystkie pliki csv automatycznie zapisaly sie w tym folderze poprzez napisanie odpowiedniego kodu.
4) Documents - folder zawierajacy plik tekstowy readme oraz zrzuty ekranu wykresow.

Opis oryginal data:
-Nazwy kolumn są tworzone w następujący sposób:
    iso2 - kraje
    year - odpowiednie lata

-poprzez połączenie "new_" oznaczajace metodę diagnozy:
    rel = nawrót
    sn = ujemny rozmaz płucny
    sp = dodatni rozmaz płucny
    ep = pozapłucny

-płeć:
    f = kobieta
    m = mężczyzna
    
-wiek:
    014 = 0-14 lat,
    1524 = 15-24 lata,
    2534 = 25 do 34 lat, 
    3544 = 35 do 44 lat,
    4554 = 45 do 54 lat, 
    5564 = 55 do 64 lat, 
    65 = 65 lat lub więcej).

