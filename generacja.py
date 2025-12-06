import random
import re

# Comprehensive Polish synthetic data pools
SYNTHETIC_DATA = {
    'name': [
        'Anna', 'Katarzyna', 'Małgorzata', 'Agnieszka', 'Barbara', 'Ewa', 'Krystyna', 'Elżbieta', 
        'Maria', 'Teresa', 'Joanna', 'Magdalena', 'Monika', 'Jadwiga', 'Danuta', 'Irena', 'Zofia',
        'Jan', 'Andrzej', 'Piotr', 'Krzysztof', 'Stanisław', 'Tomasz', 'Paweł', 'Józef', 'Marcin',
        'Marek', 'Michał', 'Grzegorz', 'Jerzy', 'Tadeusz', 'Adam', 'Łukasz', 'Zbigniew', 'Ryszard',
        'Aleksandra', 'Natalia', 'Paulina', 'Iwona', 'Beata', 'Dorota', 'Halina', 'Helena', 'Renata',
        'Wojciech', 'Dariusz', 'Henryk', 'Mariusz', 'Jacek', 'Janusz', 'Mateusz', 'Kamil', 'Dawid',
        'Karolina', 'Justyna', 'Weronika', 'Sylwia', 'Agata', 'Aneta', 'Izabela', 'Jolanta', 'Grażyna',
        'Robert', 'Rafał', 'Jakub', 'Bartosz', 'Damian', 'Sebastian', 'Adrian', 'Patryk', 'Maciej',
        'Wiktoria', 'Zuzanna', 'Julia', 'Maja', 'Lena', 'Alicja', 'Oliwia', 'Gabriela', 'Natalia',
        'Filip', 'Kacper', 'Szymon', 'Mikołaj', 'Wojtek', 'Igor', 'Dominik', 'Oskar', 'Hubert'
    ],
    
    'surname': [
        'Nowak', 'Kowalski', 'Wiśniewski', 'Wójcik', 'Kowalczyk', 'Kamiński', 'Lewandowski', 'Zieliński',
        'Szymański', 'Woźniak', 'Dąbrowski', 'Kozłowski', 'Jankowski', 'Mazur', 'Wojciechowski', 'Kwiatkowski',
        'Krawczyk', 'Kaczmarek', 'Piotrowski', 'Grabowski', 'Pawłowski', 'Michalski', 'Król', 'Wieczorek',
        'Jabłoński', 'Wróbel', 'Nowakowski', 'Majewski', 'Olszewski', 'Stępień', 'Malinowski', 'Jaworski',
        'Adamczyk', 'Dudek', 'Nowicki', 'Pawlak', 'Górski', 'Witkowski', 'Walczak', 'Sikora', 'Baran',
        'Rutkowski', 'Michalak', 'Szewczyk', 'Ostrowski', 'Tomaszewski', 'Pietrzak', 'Zalewski', 'Marciniak',
        'Wroński', 'Borkowski', 'Zawadzki', 'Kucharski', 'Szulc', 'Kubiak', 'Maciejewski', 'Szczepański',
        'Sobczak', 'Kołodziej', 'Krajewski', 'Kalinowski', 'Lis', 'Mazurek', 'Wysocki', 'Adamski',
        'Głowacki', 'Wasilewski', 'Zakrzewski', 'Sawicki', 'Chmielewski', 'Sokołowski', 'Czerwiński', 'Brzozowski',
        'Kaczmarczyk', 'Przybylski', 'Kruk', 'Domański', 'Wilk', 'Laskowski', 'Ziółkowski', 'Włodarczyk',
        'Czarnecki', 'Kozak', 'Sadowski', 'Gajewski', 'Urban', 'Baranowski', 'Kaczyński', 'Orzechowski'
    ],
    
    'age': [str(i) for i in range(18, 90)],
    
    'date-of-birth': [
        f'{d:02d}.{m:02d}.{y}' 
        for y in range(1935, 2007) 
        for m in range(1, 13) 
        for d in [1, 5, 10, 15, 20, 25]
    ][:100],
    
    'date': [
        f'{d:02d}.{m:02d}.{y}' 
        for y in range(2020, 2026) 
        for m in range(1, 13) 
        for d in [1, 5, 10, 15, 20, 25, 28]
    ][:100],
    
    'sex': ['mężczyzna', 'kobieta', 'M', 'K', 'męski', 'żeński'] * 15,
    
    'religion': [
        'katolicyzm', 'prawosławie', 'protestantyzm', 'luteranizm', 'judaizm', 'islam', 'buddyzm',
        'hinduizm', 'ateizm', 'agnostycyzm', 'niewierzący', 'rzymskokatolickie', 'greckokatolickie'
    ] * 8,
    
    'political-view': [
        'lewicowe', 'prawicowe', 'centrowe', 'liberalne', 'konserwatywne', 'socjalistyczne',
        'socjaldemokratyczne', 'chrześcijańsko-demokratyczne', 'narodowe', 'libertariańskie'
    ] * 10,
    
    'ethnicity': [
        'polska', 'ukraińska', 'białoruska', 'niemiecka', 'romska', 'litewska', 'słowacka',
        'czeska', 'rosyjska', 'żydowska', 'tatarska', 'łemkowska', 'kaszubska', 'śląska'
    ] * 8,
    
    'sexual-orientation': [
        'heteroseksualna', 'homoseksualna', 'biseksualna', 'panseksualna', 'aseksualna'
    ] * 20,
    
    'health': [
        'cukrzyca typu 2', 'nadciśnienie', 'astma oskrzelowa', 'choroba wieńcowa', 'depresja',
        'lęk uogólniony', 'migrena', 'zapalenie stawów', 'alergia pokarmowa', 'celiakia',
        'niedoczynność tarczycy', 'nadczynność tarczycy', 'choroba Hashimoto', 'udar mózgu',
        'zawał serca', 'nowotwór piersi', 'rak płuc', 'białaczka', 'epilepsja', 'choroba Parkinsona',
        'choroba Alzheimera', 'stwardnienie rozsiane', 'przewlekła obturacyjna choroba płuc', 'ADHD',
        'autyzm', 'schizofrenia', 'choroba afektywna dwubiegunowa', 'nerwica', 'bezsenność',
        'zwyrodnienie stawów', 'choroba zwyrodnieniowa kręgosłupa', 'kamica nerkowa', 'kamica żółciowa',
        'wrzodziejące zapalenie jelita grubego', 'choroba Leśniowskiego-Crohna', 'łuszczyca',
        'egzema', 'trądzik', 'zespół jelita drażliwego', 'refluks żołądkowo-przełykowy',
        'przewlekłe zapalenie żołądka', 'marskość wątroby', 'zapalenie wątroby typu B',
        'zapalenie wątroby typu C', 'HIV', 'żylaki kończyn dolnych', 'zakrzepica żył głębokich',
        'zatorowość płucna', 'niewydolność serca', 'zaburzenia rytmu serca', 'hemofilia'
    ],
    
    'relative': [
        'syn', 'córka', 'brat', 'siostra', 'ojciec', 'matka', 'dziadek', 'babcia', 'wnuk', 'wnuczka',
        'kuzyn', 'kuzynka', 'wuj', 'ciocia', 'szwagier', 'szwagierka', 'teść', 'teściowa', 
        'zięć', 'synowa', 'siostrzeniec', 'siostrzenica', 'bratanek', 'bratanica'
    ] * 4,
    
    'city': [
        'Warszawa', 'Kraków', 'Łódź', 'Wrocław', 'Poznań', 'Gdańsk', 'Szczecin', 'Bydgoszcz',
        'Lublin', 'Białystok', 'Katowice', 'Gdynia', 'Częstochowa', 'Radom', 'Sosnowiec', 'Toruń',
        'Kielce', 'Gliwice', 'Zabrze', 'Bytom', 'Olsztyn', 'Bielsko-Biała', 'Rzeszów', 'Ruda Śląska',
        'Rybnik', 'Tychy', 'Dąbrowa Górnicza', 'Płock', 'Elbląg', 'Opole', 'Gorzów Wielkopolski',
        'Wałbrzych', 'Włocławek', 'Tarnów', 'Chorzów', 'Koszalin', 'Kalisz', 'Legnica', 'Grudziądz',
        'Słupsk', 'Jaworzno', 'Jastrzębie-Zdrój', 'Nowy Sącz', 'Jelenia Góra', 'Konin', 'Piotrków Trybunalski',
        'Lubin', 'Inowrocław', 'Ostrów Wielkopolski', 'Stargard', 'Piła', 'Suwałki', 'Gniezno',
        'Ostrowiec Świętokrzyski', 'Siemianowice Śląskie', 'Siedlce', 'Mysłowice', 'Pabianice', 'Legionowo',
        'Tomaszów Mazowiecki', 'Leszno', 'Zamość', 'Pruszków', 'Chełm', 'Ełk', 'Mielec', 'Tarnowskie Góry',
        'Będzin', 'Świdnica', 'Starogard Gdański', 'Przemyśl', 'Kędzierzyn-Koźle', 'Biała Podlaska', 'Radomsko'
    ],
    
    'address': [
        f'ul. {street} {num}/{apt}, {postal} {city}'
        for street in ['Kwiatowa', 'Słoneczna', 'Leśna', 'Polna', 'Krótka', 'Długa', 'Nowa', 'Główna', 
                      'Spacerowa', 'Ogrodowa', 'Powstańców', 'Mickiewicza', 'Sienkiewicza', 'Kościuszki',
                      '3 Maja', 'Piłsudskiego', 'Dworcowa', 'Kolejowa', 'Lipowa', 'Klonowa']
        for num in range(1, 51, 5)
        for apt in [1, 5, 10, 15]
        for postal in [f'{i:02d}-{j:03d}' for i in range(10, 98, 10) for j in range(100, 901, 100)][:20]
        for city in ['Warszawa', 'Kraków', 'Poznań', 'Wrocław', 'Gdańsk']
    ][:100],
    
    'email': [
        f'{name.lower()}.{surname.lower()}@{domain}'
        for name in ['jan', 'anna', 'piotr', 'maria', 'tomasz', 'katarzyna', 'andrzej', 'ewa', 'krzysztof', 'agnieszka']
        for surname in ['kowalski', 'nowak', 'wisniewski', 'wojcik', 'lewandowski', 'kaminski', 'zielinski', 'szymanski']
        for domain in ['gmail.com', 'wp.pl', 'onet.pl', 'interia.pl', 'o2.pl']
    ][:100],
    
    'phone': [
        f'+48 {prefix} {n1:03d} {n2:03d}'
        for prefix in ['500', '501', '502', '503', '504', '505', '506', '507', '508', '509',
                       '510', '511', '512', '513', '514', '515', '516', '517', '518', '519',
                       '600', '601', '602', '603', '604', '605', '606', '607', '608', '609',
                       '660', '661', '662', '663', '664', '665', '666', '667', '668', '669',
                       '720', '721', '722', '723', '724', '725', '726', '727', '728', '729',
                       '880', '881', '882', '883', '884', '885', '886', '887', '888', '889']
        for n1 in range(100, 1000, 100)
        for n2 in range(100, 1000, 150)
    ][:100],
    
    'pesel': [
        f'{y%100:02d}{m:02d}{d:02d}{random.randint(10000, 99999)}'
        for y in range(1950, 2005, 5)
        for m in range(1, 13, 3)
        for d in [1, 10, 20]
    ][:100],
    
    'document-number': [
        f'{letter1}{letter2}{letter3}{num:06d}'
        for letter1 in 'ABCDEFGHIJK'
        for letter2 in 'LMNOPQRSTUV'
        for letter3 in 'WXYZABCDEFG'
        for num in range(100000, 999999, 100000)
    ][:100],
    
    'company': [
        'PKO Bank Polski', 'PKN Orlen', 'PGE Polska Grupa Energetyczna', 'PZU', 'Allegro',
        'InPost', 'CD Projekt', 'Cyfrowy Polsat', 'Dino Polska', 'LPP', 'Jeronimo Martins',
        'Orange Polska', 'Santander Bank Polska', 'mBank', 'Bank Pekao', 'Tauron',
        'Enea', 'Energa', 'KGHM', 'JSW', 'Lotos', 'Asseco Poland', 'Comarch', 'Play',
        'Żabka', 'Biedronka', 'Lidl Polska', 'Kaufland', 'Carrefour Polska', 'Auchan',
        'Tesco', 'Rossmann', 'Hebe', 'Media Markt', 'Saturn', 'RTV Euro AGD', 'Castorama',
        'Leroy Merlin', 'OBI', 'Decathlon', 'Reserved', 'Cropp', 'House', 'Mohito', 'Sinsay',
        'CCC', 'Eobuwie', 'Answear', 'Modivo', 'Empik', 'Wolt', 'Glovo', 'Uber', 'Bolt',
        'Revolut', 'Wise', 'Pracuj.pl', 'OLX', 'Vinted', 'Booking.com', 'Airbnb', 'LOT',
        'Ryanair', 'Wizzair', 'PKP Intercity', 'PKP Cargo', 'Poczta Polska', 'DHL', 'DPD',
        'FedEx', 'UPS', 'GLS', 'Allegro Smart', 'Amazon', 'Zalando', 'Nike', 'Adidas',
        'H&M', 'Zara', 'Mango', 'Parfois', 'Douglas', 'Sephora', 'McDonald\'s', 'KFC',
        'Burger King', 'Subway', 'Pizza Hut', 'Domino\'s Pizza', 'Starbucks', 'Costa Coffee'
    ],
    
    'school-name': [
        'I Liceum Ogólnokształcące im. Adama Mickiewicza', 
        'II Liceum Ogólnokształcące im. Marii Skłodowskiej-Curie',
        'III Liceum Ogólnokształcące im. Juliusza Słowackiego',
        'IV Liceum Ogólnokształcące im. Henryka Sienkiewicza',
        'V Liceum Ogólnokształcące im. Stanisława Staszica',
        'Technikum Nr 1', 'Technikum Nr 2', 'Technikum Informatyczne',
        'Szkoła Podstawowa Nr 1', 'Szkoła Podstawowa Nr 5', 'Szkoła Podstawowa Nr 10',
        'Gimnazjum Nr 1', 'Gimnazjum Nr 3', 'Gimnazjum Nr 7',
        'Zespół Szkół Technicznych', 'Zespół Szkół Ekonomicznych',
        'Zespół Szkół Mechanicznych', 'Zespół Szkół Gastronomicznych',
        'Politechnika Warszawska', 'Politechnika Krakowska', 'Politechnika Wrocławska',
        'Politechnika Gdańska', 'Politechnika Poznańska', 'Politechnika Łódzka',
        'Uniwersytet Warszawski', 'Uniwersytet Jagielloński', 'Uniwersytet Wrocławski',
        'Uniwersytet im. Adama Mickiewicza w Poznaniu', 'Uniwersytet Łódzki',
        'Akademia Górniczo-Hutnicza', 'Szkoła Główna Handlowa', 'Uniwersytet Ekonomiczny w Krakowie',
        'Akademia Medyczna', 'Uniwersytet Medyczny', 'Akademia Sztuk Pięknych',
        'Akademia Muzyczna', 'Akademia Teatralna', 'Akademia Wychowania Fizycznego'
    ] * 2,
    
    'job-title': [
        'dyrektor', 'kierownik', 'specjalista', 'konsultant', 'analityk', 'programista',
        'inżynier', 'technolog', 'konstruktor', 'projektant', 'administrator', 'koordynator',
        'menedżer', 'lekarz', 'pielęgniarka', 'nauczyciel', 'wykładowca', 'profesor',
        'asystent', 'sekretarka', 'księgowy', 'księgowa', 'prawnik', 'radca prawny',
        'sprzedawca', 'handlowiec', 'przedstawiciel handlowy', 'agent', 'makler', 'broker',
        'magazynier', 'logistyk', 'operator', 'mechanik', 'elektryk', 'hydraulik',
        'stolarz', 'malarz', 'murarz', 'spawacz', 'ślusarz', 'kierowca', 'kurier',
        'kasjer', 'recepcjonista', 'kelner', 'kucharz', 'barman', 'opiekun', 'opiekunka',
        'pracownik biurowy', 'pracownik produkcji', 'pracownik ochrony', 'strażnik', 'ochroniarz',
        'informatyk', 'tester', 'deweloper', 'designer', 'grafik', 'copywriter', 'redaktor',
        'dziennikarz', 'fotograf', 'operator kamery', 'reżyser', 'producent', 'aktor',
        'muzyk', 'wokalista', 'tłumacz', 'psycholog', 'terapeuta', 'fizjoterapeuta',
        'dietetyk', 'trener personalny', 'instruktor', 'kosmetyczka', 'fryzjer', 'stylistka'
    ],
    
    'bank-account': [
        f'{p1:02d} {p2:04d} {p3:04d} {p4:04d} {p5:04d} {p6:04d} {p7:04d}'
        for p1 in range(10, 99, 10)
        for p2 in range(1000, 9999, 1000)
        for p3 in range(1000, 9999, 2000)
        for p4 in range(1000, 9999, 2000)
        for p5 in range(1000, 9999, 2000)
        for p6 in range(1000, 9999, 2000)
        for p7 in range(1000, 9999, 2000)
    ][:100],
    
    'credit-card-number': [
        f'{p1:04d} {p2:04d} {p3:04d} {p4:04d}'
        for p1 in [4000, 5100, 5200, 3700, 6011]
        for p2 in range(1000, 9999, 500)
        for p3 in range(1000, 9999, 500)
        for p4 in range(1000, 9999, 500)
    ][:100],
    
    'username': [
        f'{prefix}{num}{suffix}'
        for prefix in ['user', 'player', 'gamer', 'pro', 'master', 'king', 'queen', 'boss', 'admin', 'moderator']
        for num in range(100, 1000, 100)
        for suffix in ['', '_pl', '_2024', '_official', '_real', '_original', 'PL', '123', 'XD', '_gaming']
    ][:100],
    
    'secret': [
        f'{word1}{word2}{num}!'
        for word1 in ['Haslo', 'Password', 'Bezpieczne', 'Tajne', 'Sekretne', 'Super', 'Mega', 'Ultra']
        for word2 in ['123', '456', '789', '2024', '2025', 'Xyz', 'Abc', 'Qwe']
        for num in range(10, 100, 10)
    ][:100]
}


def fill_synthetic_data(text: str, randomize: bool = True) -> str:
    """
    Fills placeholders in text with synthetic data.
    
    Args:
        text: Input text with placeholders in format [entity-type]
        randomize: If True, selects random values; if False, uses sequential values
    
    Returns:
        Text with placeholders replaced by synthetic data
    
    Example:
        >>> fill_synthetic_data("[name] ma kota w [city]")
        'Anna ma kota w Warszawa'
    """
    result = text
    
    # Find all placeholders in the text with square brackets
    placeholders = re.findall(r'\[([^\]]+)\]', text)
    
    # Replace each placeholder
    for placeholder in placeholders:
        entity_type = placeholder.strip()
        
        if entity_type in SYNTHETIC_DATA:
            if randomize:
                replacement = random.choice(SYNTHETIC_DATA[entity_type])
            else:
                # For non-random, cycle through values
                index = hash(text + entity_type) % len(SYNTHETIC_DATA[entity_type])
                replacement = SYNTHETIC_DATA[entity_type][index]
            
            # Replace only the first occurrence to handle multiple same placeholders differently
            result = result.replace(f'[{entity_type}]', replacement, 1)
    
    return result


# Example usage and tests
if __name__ == "__main__":
    # Test examples
    test_texts = [
        "[name] ma kota w [city]",
        "Pacjent [name] [surname], PESEL: [pesel], ur. [date-of-birth]",
        "Kontakt: [email], tel. [phone]",
        "Adres: [address]",
        "Diagnoza: [health], przyjęto [date]",
        "[name] [surname] pracuje jako [job-title] w [company]",
        "Mój [relative] [name] mieszka w [city]",
        "Wyznanie: [religion], orientacja: [sexual-orientation]",
        "Numer karty: [credit-card-number], konto: [bank-account]"
    ]
    
    print("=== Przykłady zastosowania ===\n")
    for text in test_texts:
        filled = fill_synthetic_data(text)
        print(f"Wejście:  {text}")
        print(f"Wyjście:  {filled}\n")
    
    # Show multiple random generations
    print("=== Wielokrotne losowe generowanie ===\n")
    sample_text = "[name] [surname] z [city] choruje na [health]"
    print(f"Szablon: {sample_text}\n")
    for i in range(5):
        print(f"{i+1}. {fill_synthetic_data(sample_text)}")


    sample_text = "[name] [surname] z [city] choruje na [health]"
    print(f"{fill_synthetic_data(sample_text)}")