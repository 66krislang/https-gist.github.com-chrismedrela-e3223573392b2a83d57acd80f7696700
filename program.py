# PIT roczny
# PLN
# USD -> PLN

# 1) wybór język programowania
# 2) kodowanie = programowanie
# 3) testowanie = QA (Quality Assurance) = kontrola jakości

# W terminalu:
# python program.py
# clear

# http://api.nbp.pl/api/exchangerates/rates/{table}/{code}/today/
# http://api.nbp.pl/api/exchangerates/rates/a/usd/today/?format=json

# A = kurs średnich
# B = kurs sprzedaży i wymiany

# 1. idziemy do castoramy po skrzynkę z narzędziami (i wiertarką) i przynosimy do domu: w terminalu: pip install requests
# 2. wyciągamy ze skrzynki wiertarkę i kładziemy na biurku
# 3. używamy wiertarki

# dane = {
#     "table": "A",
#     "currency": "dolar amerykański",
#     "code": "USD",
#     "rates": [
#         {
#             "no": "123/A/NBP/2023",
#             "effectiveDate": "2023-06-28",
#             "mid": 4.0719
#         }
#     ]
# }




from requests import get

print("KALKULATOR WALUT")

waluta = input("Podaj walutę: ")

strona = get(f"http://api.nbp.pl/api/exchangerates/rates/a/{waluta}/today/?format=json")

dane = strona.json()

kurs = dane["rates"][0]["mid"]

print(f"1 {waluta} = {kurs} PLN")
