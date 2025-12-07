# Dokumentacja prac nad projektem

## Eksploracja i korekta zbioru danych
Dostarczone datasety zostały przejrzane, zeby zapoznać się z ich strukturą. Zostało odnalezione wiele błędów związanych m.in. ze spójnością i sensownością danych. Część danych (zarówno na wejściu, jak i na wyjściu) została poddana korekcie. Szczegóły opisano w pliku dataset.md. Poprawione dane znajdują się w plikach data_1.txt (pełne dane) i data_2.txt

## Reanotacja danych
Po wielu nieudanych próbach zrównoleglenia danych z plików data_1.txt i data_2.txt dane zostały częściowo zreanotowane ręcznie za pomocą narzędzia https://arunmozhi.in/ner-annotator/. Następnie wyeksportowane dane zostały przekształcone przy użyciu skryptu sample_data_transformation.py w format odpowiedni do późniejszego trenowania modelu przy użyciu biblioteki spaCy. 

## Trening danych
Proces trenowania jest udokumentowany w pliku training.py. Za pomocą skryptu testing.py została przeprowadzona wstępna inspekcja jakości na fragmencie, który nie został zaanotowany w poprzedniej części.

============================= Training pipeline =============================
ℹ Pipeline: ['tok2vec', 'ner']
ℹ Initial learn rate: 0.001
E    #       LOSS TOK2VEC  LOSS NER  ENTS_F  ENTS_P  ENTS_R  SCORE 
---  ------  ------------  --------  ------  ------  ------  ------
  0       0          0.00     85.26    0.00    0.00    0.00    0.00
  1     200       1119.35   3977.76   34.89   46.10   28.06    0.35
  3     400       3756.25   1841.34   57.26   60.26   54.55    0.57
  5     600       7120.52   1123.15   55.86   60.65   51.78    0.56
  7     800        573.38    845.93   61.47   65.77   57.71    0.61
  9    1000       1486.53    829.37   60.00   64.98   55.73    0.60
 13    1200      11362.58    702.06   64.46   67.53   61.66    0.64

## Stworzenie skryptu anonimizującego dane
