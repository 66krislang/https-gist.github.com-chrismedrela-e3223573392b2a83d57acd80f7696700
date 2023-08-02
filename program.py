# PIT roczny

# PLN
# USD -> PLN

# 1) wybór języka programowania
# 2) kodowanie = programowanie
# 3) testowanie = QA (Quality Assurance) = kontrola jakości

# Lewa = program = przepis kulinarny

# Prawa = terminal = robot w kuchnii

# W terminalu:
# python program.py  # wypiecz ciastko
# clear  # posprzątaj kuchnię

# Mario Bros = platformówka

# http://api.nbp.pl/api/exchangerates/rates/{table}/{code}/today/
# http://api.nbp.pl/api/exchangerates/rates/a/usd/today/?format=json

# A = kursy średnich
# B = kursów sprzedaży i zakupu

# 1. idziemy do Castoramy po skrzynkę z narzędziami (z wiertarką) i przynosimy skrzynkę do domu: pip install requests
# 2. wyciągamy wiertarkę ze skrzynki i kładziemy na biurku: from skrzynka import wiertarka
# 3. używamy wiertarki

# dane = {
#     "table": "A",
#     "currency": "dolar amerykański",
#     "code": "USD",
#     "rates": [
#         {
#             "no": "148/A/NBP/2023",
#             "effectiveDate": "2023-08-02",
#             "mid": 4.0497
#         }
#     ]
# }

# Edytor kodu:
# Visual Studio Code
# PyCharm



from requests import get

print("KALKULATOR WALUT")

waluta = input("Podaj walutę: ")

strona = get(f"http://api.nbp.pl/api/exchangerates/rates/a/{waluta}/today/?format=json")

dane = strona.json()

kurs = dane["rates"][0]["mid"]

print(f"1 {waluta} = {kurs} pln")
