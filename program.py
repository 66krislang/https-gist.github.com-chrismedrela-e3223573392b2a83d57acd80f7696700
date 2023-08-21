# PIT roczny

# PLN
# USD => PLN

# 1) wybór język programowania: łatwy i popularny
# 2) programowanie = kodowanie
# 3) testowanie = QA (Quality Assurance) = kontrola jakości

# Po lewej = program = przepis kulinarny

# Po prawej = terminal = kuchnia z robotem kuchennym

# W terminalu:
# python program.py  # uruchomienie programu = naciśnięcie play na robocie kuchennym
# clear   # wyczyszczenie terminala = posprzątanie kuchnii
# pip install requests  # instalacja biblioteki = pójście do castoramy

# http://api.nbp.pl/api/exchangerates/rates/{table}/{code}/today/
# http://api.nbp.pl/api/exchangerates/rates/a/usd/today/?format=json

# A = kursy średnie
# B = kursy zakupu i sprzedaży

# 1. Idziemy do Castoramy po skrzynkę z narzędziami z wiertarką i przynosimy do domu.
# 2. Wyciągamy ze skrzynki wiertarkę i kładziemy na biurku
# 3. Używamy wiertarki.

# dane = {
#     "table": "A",
#     "currency": "dolar amerykański",
#     "code": "USD",
#     "rates": [
#         {
#             "no": "160/A/NBP/2023",
#             "effectiveDate": "2023-08-21",
#             "mid": 4.1124
#         }
#     ]
# }



from requests import get

print("KALKULATOR WALUT")

waluta = input("Podaj walutę: ")

strona = get(f"http://api.nbp.pl/api/exchangerates/rates/a/{waluta}/today/?format=json")

dane = strona.json()

kurs = dane["rates"][0]["mid"]

print(f"1 {waluta} = {kurs} pln")
