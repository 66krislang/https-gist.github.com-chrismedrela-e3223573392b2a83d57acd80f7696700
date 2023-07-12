# PIT (roczny)
#
# PLN
# EUR -> PLN
# USD -> PLN

# 1) wybór języka programowania
# 2) programujemy = kodujemy
# 3) testowanie = QA (Quality Assurance) = kontrola jakość

# W terminalu (= kuchnii):
# python program.py
# clear
# pip install requests

# http://api.nbp.pl/api/exchangerates/rates/{table}/{code}/today/
# http://api.nbp.pl/api/exchangerates/rates/a/usd/today/?format=json

# A = kurs średni
# B = kurs sprzedaży i kupna

# 1. przynieść skrzynkę z narzędziami (z wiertarką) z castoramy
# 2. ze skrzynki wyciągamy wiertarkę na stół
# 3. używamy wiertarki

# dane = {
#     "table": "A",
#     "currency": "dolar amerykański",
#     "code": "USD",
#     "rates": [
#         {
#             "no": "133/A/NBP/2023",
#             "effectiveDate": "2023-07-12",
#             "mid" :4.0347
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
