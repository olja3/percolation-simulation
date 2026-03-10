# Symulacja perkolacji – README

## 1. Definicja perkolacji

Perkolacja to zjawisko powstawania połączonej struktury, nazywanej klastrem w losowym ośrodku.  
W modelu zastosowanym w tym projekcie ośrodkiem jest dwuwymiarowa siatka n × n, w której każde pole:
- jest otwarte z prawdopodobieństwem p,
- jest zamknięte z prawdopodobieństwem 1 − p.

Wtedy perkolację definiujemy jako ciągłą ścieżkę otwartych pól łączącą górny i dolny brzeg siatki.


## 2. Zastosowania perkolacji

Modele perkolacyjne znajdują zastosowanie m.in. w:
- fizyce, przepływ cieczy przez porowate ośrodki,
- geologii, przenikanie wody lub ropy przez skały,
- biologii, rozprzestrzenianie się chorób,
- sieciach komputerowych, odporność sieci na awarie,
- socjologii, rozchodzenie się informacji w sieciach społecznych,
- materiałoznawstwie, przewodnictwo w materiałach kompozytowych.

Tego typu symulacje mogą przedstawiać na przykład czy epidemia obejmie cały obszar, czy sieć pozostanie spójna po losowych uszkodzeniach.


## 3. Działanie programu

Program:
1. Generuje losowe konfiguracje siatki dla zadanej wartości p.
2. Wyszukuje klastry otwartych pól metodą BFS.
3. Sprawdza, czy którykolwiek klaster łączy górny i dolny brzeg.
4. Powtarza symulację wiele razy dla tego samego p.
5. Oblicza częstość perkolacji oraz średni rozmiar największego klastra.
6. Powtarza całość dla różnych wartości p.

Dodatkowo program umożliwia graficzną analizę struktury klastrów, w tym wyróżnienie klastra perkolującego.


## 4. Interpretacja wykresów (wyniki symulacji)

### Wykres „Perkolacja vs p”
- Oś X: prawdopodobieństwo otwarcia pola p,
- Oś Y: częstość występowania perkolacji.

Na podstawie uzyskanych wyników można zauważyć, że:
- dla małych wartości p < 0.5 perkolacja praktycznie nie występuje, co oznacza, że otwarte pola tworzą jedynie małe, izolowane klastry,
- w zakresie p ≈ 0.55–0.65 obserwowany jest gwałtowny wzrost częstości perkolacji, co odpowiada zjawisku krytycznemu, zachowanie to jest zgodne z teoretycznym progiem perkolacji dla nieskończonej siatki kwadratowej, wynoszącym p ≈ 0.59,
- dla dużych wartości p > 0.65 perkolacja zachodzi niemal zawsze, ponieważ większość pól jest otwarta i tworzy jeden dominujący klaster.


### Wykres „Największy klaster vs p”
- Oś X: prawdopodobieństwo p,
- Oś Y: średni rozmiar największego klastra.

Analiza wykresu pokazuje, że:
- dla małych wartości p największe klastry są niewielkie i rosną powoli,
- w pobliżu progu perkolacji następuje gwałtowny wzrost rozmiaru największego klastra,
- dla większych p jeden klaster obejmuje znaczną część siatki, co świadczy o dominacji jednego połączonego obszaru.

Zjawisko to jest charakterystyczne dla przejść fazowych i potwierdza poprawność działania symulacji.


## 5. Interpretacja rysunków siatki (wizualizacja wyników)

### Konfiguracja perkolacji (czarno-biała)
- białe pola – pola otwarte,
- czarne pola – pola zamknięte.

Rysunek przedstawia pojedynczą losową siatkę dla wartości p=0.6. Na jego podstawie można wizualnie ocenić stopień połączenia pól, jednak jednoznaczne stwierdzenie perkolacji wymaga analizy klastrów wykonanej przez program.


### Wizualizacja klastrów 
- każde pole ma kolor zależny od rozmiaru klastra, do którego należy,
- skala barwna przedstawia liczbę pól w klastrze.

Na wizualizacjach dla różnych wartości p można zauważyć, że:
- dla p = 0.4 układ znajduje się poniżej progu perkolacji, dlatego powstaje wiele małych, izolowanych klastrów, a brak jest klastra dominującego zdolnego do połączenia górnego i dolnego brzegu siatki,
- dla p = 0.6 pojawia się jeden wyraźnie większy klaster, który często odpowiada klastrowi perkolującemu,
- dla p = 0.7 jeden klaster dominuje nad pozostałymi i obejmuje znaczną część siatki.

Wizualizacja klastrów pozwala zaobserwować moment przejścia od struktury rozproszonej do układu z klastrem dominującym, charakterystyczny dla zjawiska perkolacji.

### Wyróżnienie klastra perkolującego
W przypadku, gdy w układzie występuje perkolacja, klaster perkolujący jest dodatkowo wyróżniany kolorem czerwonym na tle pozostałych pól. Takie wyróżnienie pozwala jednoznacznie wskazać, który klaster odpowiada za perkolację oraz ułatwia wizualną analizę struktury układu, szczególnie w pobliżu progu krytycznego.



