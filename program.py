# Język programowania (Python):  https://www.python.org/downloads/
# Edytor kodu (Word dla programistów) - Visual Studio Code  https://code.visualstudio.com

# zeznanie podatkowe
# PLN
# USD -> PLN
# EUR -> PLN

# 1) wybór język programowania
# 2) programowanie = kodowanie
# 3) QA (Quality Assurance) = testowanie = kontrola jakości

# W terminalu:
# python program.py
# clear / cls
# pip install requests

# http://api.nbp.pl/api/exchangerates/rates/{table}/code}/{date}/
# http://api.nbp.pl/api/exchangerates/rates/a/usd/2023-05-29/?format=json

# A = kursów średnich
# B = kursów zakupu / sprzedaży

# 1. wziąć z Castoramy do domu skrzynkę z narzędziami (wiertarką)
# 2. ze skrzynki wyciągnąć wiertarkę i położyć na biurku
# 3. użyć wiertarki

# dane = {
#     "table": "A",
#     "currency": "dolar amerykański",
#     "code": "USD",
#     "rates": [
#         {
#             "no": "102/A/NBP/2023",
#             "effectiveDate": "2023-05-29",
#             "mid": 4.2234
#         }
#     ]
# }




from requests import get

print("KALKULATOR WALUT")

waluta = input("Podaj walutę: ")

dzien = input("Podaj dzień (RRRR-MM-DD): ")

strona = get(f"http://api.nbp.pl/api/exchangerates/rates/a/{waluta}/{dzien}/?format=json")

dane = strona.json()

kurs = dane["rates"][0]["mid"]

print(f"1 {waluta} = {kurs} PLN w dniu {dzien}")