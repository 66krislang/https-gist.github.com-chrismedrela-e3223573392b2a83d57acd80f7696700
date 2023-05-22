# PLN
# EUR -> PLN
# USD -> PLN

# 1. wybór języka programowania
# 2. kodowanie = programowanie
# 3. testowanie = QA (Quality Assurance) = kontrola jakości

# Język programownia (Python):  https://www.python.org/downloads/
# Edytor kodu (Word dla programistów): Visual Studio Code  https://code.visualstudio.com

# W terminalu:
# python program.py
# clear / cls
# pip install requests

# http://api.nbp.pl/api/exchangerates/rates/{table}/code}/{date}/
# http://api.nbp.pl/api/exchangerates/rates/a/usd/2023-05-22/?format=json


# 1. idziemy do Castoramy po skrzynkę z narzędziami, m.in. z wiertarką: pip install requests (w terminalu!)
# 2. wyciągamy ze skrzynki wiertarkę i kładziemy na stole
# 3. używamy wiertarki

# dane = {
#     "table": "A",
#     "currency": "dolar amerykański",
#     "code": "USD",
#     "rates": [
#         {
#             "no": "097/A/NBP/2023",
#             "effectiveDate": "2023-05-22",
#             "mid": 4.1881
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

