import regex as re
"""
Docstring for transformation
INPUT_1:
POUCZENIE 1 Inwestor jest obowiązany zawiadomić o zamierzonym terminie rozpoczęcia robót budowlanych na które jest wymagane pozwolenie na budowę właściwy organ nadzoru budowlanego oraz projektanta sprawującego nadzór nad zgodnością realizacji budowy z projektem co najmniej na 7 dni przed ich rozpoczęciem dołączając na piśmie 1 oświadczenie kierownika budowy robót stwierdzające sporządzenie planu bezpieczeństwa i ochrony zdrowia oraz przyjęcie obowiązku kierowania budową robotami budowlanymi a także zaświadczenie o którym mowa w art 12 ust 7 ustawy Prawo budowlane 2 w przypadku ustanowienia nadzoru inwestorskiego oświadczenie inspektora nadzoru inwestorskiego stwierdzające przyjęcie obowiązku pełnienia nadzoru inwestorskiego nad danymi robotami budowlanymi a także zaświadczenie o którym mowa w art 12 ust 7 ustawy Prawo budowlane 3 informacje zawierające dane zamieszczone w ogłoszeniu o którym mowa w art 42 ust 2 pkt 2 ustawy Prawo budowlane 2 Inwestor może przystąpić do użytkowania obiektu przed wykonaniem wszystkich robót budowlanych pod warunkiem uzyskania pozwolenia na użytkowanie wydanego przez właściwy organ nadzoru budowlanego 3 Przed wydaniem pozwolenia na użytkowanie obiektu właściwy organ nadzoru budowlanego przeprowadzi obowiązkową kontrolę budowy zgodnie z art 59a ustawy Prawo budowlane Wniosek o udzielenie pozwolenia na użytkowanie stanowi wezwanie właściwego organu do przeprowadzenia obowiązkowej kontroli Sprawę prowadzi [name] [surname] Tel [phone] pok 005 Zwolnione od opłaty skarbowej zgodnie z art 7 pkt 3 ustawy z dnia 16 11 2006r o opłacie skarbowej Dz U 06 225 1635 Załączniki Nr 1 Projekt budowlany 2 egz Otrzymują 1 Związek Międzygminny PUSZCZA ZIELONKA z załącznikami przez Pełnomocnika 2 GMINA [city] [address] Do wiadomości 1 Burmistrz Miasta i Gminy w [city] 2 Wielkopolski Wojewódzki Konserwator Zabytków w [city] [address] PINB 1 egz projektu Jeśli nie zachodzą wymienione okoliczności lub potrzeba skreślić Niepotrzebne skreślić
INPUT_2:
POUCZENIE 1 Inwestor jest obowiązany zawiadomić o zamierzonym terminie rozpoczęcia robót budowlanych, na które jest wymagane pozwolenie na budowę, właściwy organ nadzoru budowlanego oraz projektanta sprawującego nadzór nad zgodnością realizacji budowy z projektem co najmniej na 7 dni przed ich rozpoczęciem, dołączając na piśmie 1 oświadczenie kierownika budowy robót stwierdzające sporządzenie planu bezpieczeństwa i ochrony zdrowia oraz przyjęcie obowiązku kierowania budową robotami budowlanymi, a także zaświadczenie, o którym mowa w art 12 ust 7 ustawy Prawo budowlane 2 w przypadku ustanowienia nadzoru inwestorskiego oświadczenie inspektora nadzoru inwestorskiego stwierdzające przyjęcie obowiązku pełnienia nadzoru inwestorskiego nad danymi robotami budowlanymi, a także zaświadczenie, o którym mowa w art 12 ust 7 ustawy Prawo budowlane 3 informacje zawierające dane zamieszczone w ogłoszeniu, o którym mowa w art 42 ust 2 pkt 2 ustawy Prawo budowlane 2 Inwestor może przystąpić do użytkowania obiektu przed wykonaniem wszystkich robót budowlanych pod warunkiem uzyskania pozwolenia na użytkowanie wydanego przez właściwy organ nadzoru budowlanego 3 Przed wydaniem pozwolenia na użytkowanie obiektu właściwy organ nadzoru budowlanego przeprowadzi obowiązkową kontrolę budowy zgodnie z art 59a ustawy Prawo budowlane Wniosek o udzielenie pozwolenia na użytkowanie stanowi wezwanie właściwego organu do przeprowadzenia obowiązkowej kontroli Sprawę prowadzi Apolonia Kościesza Tel 574 777 072 pok 005 Zwolnione od opłaty skarbowej zgodnie z art 7 pkt 3 ustawy z dnia 16 11 2006r o opłacie skarbowej Dz U 06 225 1635 Załączniki Nr 1 Projekt budowlany 2 egz Otrzymują 1 Związek Międzygminny PUSZCZA ZIELONKA z załącznikami przez Pełnomocnika 2 GMINA Nowa Ruda al. Słonecznikowa 27 10-776 Elbląg Do wiadomości 1 Burmistrz Miasta i Gminy w Oleśnica 2 Wielkopolski Wojewódzki Konserwator Zabytków w Polkowice pl. 1askółcza 90 69-948 Toruń PINB 1 egz projektu Jeśli nie zachodzą wymienione okoliczności lub potrzeba skreślić Niepotrzebne skreślić
OUTPUT:
[
    [
        "POUCZENIE 1 Inwestor jest obowiązany zawiadomić o zamierzonym terminie rozpoczęcia robót budowlanych, na które jest wymagane pozwolenie na budowę, właściwy organ nadzoru budowlanego oraz projektanta sprawującego nadzór nad zgodnością realizacji budowy z projektem co najmniej na 7 dni przed ich rozpoczęciem, dołączając na piśmie 1 oświadczenie kierownika budowy robót stwierdzające sporządzenie planu bezpieczeństwa i ochrony zdrowia oraz przyjęcie obowiązku kierowania budową robotami budowlanymi, a także zaświadczenie, o którym mowa w art 12 ust 7 ustawy Prawo budowlane 2 w przypadku ustanowienia nadzoru inwestorskiego oświadczenie inspektora nadzoru inwestorskiego stwierdzające przyjęcie obowiązku pełnienia nadzoru inwestorskiego nad danymi robotami budowlanymi, a także zaświadczenie, o którym mowa w art 12 ust 7 ustawy Prawo budowlane 3 informacje zawierające dane zamieszczone w ogłoszeniu, o którym mowa w art 42 ust 2 pkt 2 ustawy Prawo budowlane 2 Inwestor może przystąpić do użytkowania obiektu przed wykonaniem wszystkich robót budowlanych pod warunkiem uzyskania pozwolenia na użytkowanie wydanego przez właściwy organ nadzoru budowlanego 3 Przed wydaniem pozwolenia na użytkowanie obiektu właściwy organ nadzoru budowlanego przeprowadzi obowiązkową kontrolę budowy zgodnie z art 59a ustawy Prawo budowlane Wniosek o udzielenie pozwolenia na użytkowanie stanowi wezwanie właściwego organu do przeprowadzenia obowiązkowej kontroli Sprawę prowadzi Apolonia Kościesza Tel 574 777 072 pok 005 Zwolnione od opłaty skarbowej zgodnie z art 7 pkt 3 ustawy z dnia 16 11 2006r o opłacie skarbowej Dz U 06 225 1635 Załączniki Nr 1 Projekt budowlany 2 egz Otrzymują 1 Związek Międzygminny PUSZCZA ZIELONKA z załącznikami przez Pełnomocnika 2 GMINA Nowa Ruda al. Słonecznikowa 27 10-776 Elbląg Do wiadomości 1 Burmistrz Miasta i Gminy w Oleśnica 2 Wielkopolski Wojewódzki Konserwator Zabytków w Polkowice pl. 1askółcza 90 69-948 Toruń PINB 1 egz projektu Jeśli nie zachodzą wymienione okoliczności lub potrzeba skreślić Niepotrzebne skreślić",
        {
            "entities": [
                [
                    1465,
                    1473,
                    "name"
                ],
                [
                    1474,
                    1483,
                    "surname"
                ],
                [
                    1488,
                    1499,
                    "surname"
                ]
            ]
        }
    ]
]
"""

def extract_labels(file):
    with open(file, 'r') as f:
        content = f.read()
    labels = re.findall(r'\[[^[]*\]',content)
    labels = set(labels)
    print(labels)
    return labels

def split_into_paragraphs(file_1, file_2): #file_1 – original data, #file_2 – anonymised
    pairs = {}
    with open(file_1, 'r') as f:
        original = f.read().split("\n")
    
    with open(file_2, 'r') as f:
        anon = f.read().split("\n")

    for i, paragraph in enumerate(original):
        if paragraph:
            pairs[paragraph]=anon[i]

    print(pairs)
    

#def transform_labels(file_1, file_2): #file_1 – original data, #file_2 – anonymised

if __name__=="__main__":
    #extract_labels("content/data_2.txt")
    labels = {'[ethnicity]', '[sector]', '[social-media]', '[science]', '[surname_2]', '[school-name]', '[missing-part]', '[travel]', '[discovery]', '[amount]', '[version]', '[sexual-orientation]', '[name-of-product]', '[ID number]', '[pesel]', '[name]', '[product]', '[address]', '[document-number]', '[subject]', '[app-name]', '[sport-discipline]', '[time]', '[country2]', '[health]', '[gratitude]', '[company]', '[platform-name]', '[marka]', '[yes/no]', '[weight-loss/muscle-gain]', '[website]', '[standard-name]', '[viral]', '[networking]', '[political-view]', '[vegetarian/vegan]', '[healthcare-professional]', '[size]', '[year]', '[name_2]', '[credit-card-number]', '[percentage]', '[programming-language]', '[newfollowers]', '[religion]', '[country]', '[genre]', '[education]', '[date-of-birth]', '[username]', '[social-media-username]', '[introduction]', '[system-version]', '[website-url]', '[sport]', '[name_1]', '[data]', '[industry]', '[text]', '[food]', '[debt]', '[culture]', '[product-name]', '[research]', '[field]', '[data-analysis]', '[#missingperson]', '[higher-amount]', '[secret]', '[link]', '[phone]', '[age]', '[social-media-platform]', '[podcast]', '[initials]', '[scientist-name]', '[sex]', '[country1]', '[teamwork]', '[vin]', '[time-range]', '[city]', '[email]', '[tak/nie]', '[censorship]', '[department]', '[grade]', '[promo-code]', '[surname_1]', '[bank-account]', '[finance]', '[#health]', '[#city]', '[software]', '[country3]', '[hobby]', '[number]', '[demographics]', '[surname]', '[last-digit]', '[count]', '[job-title]', '[#political-view]', '[relative]', '[model]', '[specific-task]', '[street]', '[public-place]', '[date]', '[active/sedentary]', '[answer]'}
    split_into_paragraphs("content/data_1.txt", "content/data_2.txt")