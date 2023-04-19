# Język programowania Python: https://www.python.org/downloads/
# Edytor kodu (Word dla programistów): Visual Studio Code  https://code.visualstudio.com

# dochód = przychód - koszty

# PLN USD EUR

# USD -> PLN
# EUR -> PLN

# Narodowy Bank Polski

# W terminalu:
# python program.py
# clear
# pip install requests

# 1) wybiera język programowania
# 2) kodowanie = programowanie
# 3) testowanie = QA (Quality Assurance) = kontrola jakości

# 1. idziemy do Castoramy po skrzynkę z narzędziami
# 2. wyciągamy ze skrzynki wiertarkę i kładziemy na biurku
# 3. używamy wiertarki

# from skrzynka import wiertarka

from requests import get

print("KALKULATOR WALUT")

waluta = input("Podaj walutę: ")

dzien = input("Podaj dzień (RRRR-MM-DD): ")

strona = get(f"http://api.nbp.pl/api/exchangerates/rates/a/{waluta}/{dzien}/?format=json")

dane = strona.json()

kurs = dane["rates"][0]["mid"]

print(f"1 {waluta} = {kurs} PLN w dniu {dzien}")

# http://api.nbp.pl/api/exchangerates/rates/{table}/{code}/{date}/
# http://api.nbp.pl/api/exchangerates/rates/a/usd/2023-04-19/?format=json

# A = kursów średnich
# B = kursów sprzedaży i kupna

# dane = {
#     "table": "A",
#     "currency": "dolar amerykański",
#     "code": "USD",
#     "rates": [
#         {
#             "no": "076/A/NBP/2023",
#             "effectiveDate": "2023-04-19",
#             "mid": 4.2244
#         }
#     ]
# }