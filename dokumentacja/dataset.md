# Błędy w datasecie

## Niespójność metodologiczna niektórych klas
Niespójność ta zdaje się dotyczyć przede wszystkim klas [health] i [relative].

## Tagi z klas spoza zdefiniowanych w zadaniu

W zanonimizowanym datasecie pojawiały się klasy takie jak:
* [ID number]
* [country]
* [industry]
* [#health]
którym w oryginalnym tekście najczęściej odpowiadały placeholdery: idenytczne z nadmiarowym tagiem, tylko bez nawiasów kwadratowych, lub podobne, np. w innym języku lub z podmienionymi znakami. Niektóre nadmiarowe tagi zawierały hashtagi przypominające tagi słuzace do anonimizacji.

W takim przypadku tagi w nawiasach kwadratowych ze zanonimizowanego zostały zastąpione odpowiadającym im fragmentom danych przed anonimizacją

### Przykład 1
Dataset oryginalny:
Podrzucam też jego PESEL (99111467505) i nr dowodu (ID num8er), bo właściciel chce to wszystko sprawdzić.
Dataset zanonimizowany:
Podrzucam też jego PESEL ([pesel]) i nr dowodu ([ID number]), bo właściciel chce to wszystko sprawdzić.

## Rózna liczba spacji
Analogiczne fragmenty datasetu przed normalizacją i po zawierały czasem rózne liczby spacji w odpowiadających sobie fragmentach. Nie jest to duzy problem, ale dla bardziej spojnego datasetu wszystkie wielokrotne spacje zostały zastąpione pojedynczą.

## Mało zróznicowane domeny adresów mailowych
Wszystkie lub większość adresów w oryginalnych tekstach ma domenę @example.com lub @example.net, co moze powodować małą elastyczność względem realnych danych. Część adresów w oryginalnych danych została zastąpiona bardziej zrónicowanymi domenami, takimi jak @wp.pl czy @gmail.com.