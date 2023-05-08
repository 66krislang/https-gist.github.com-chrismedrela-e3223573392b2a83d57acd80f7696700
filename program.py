# Zeznanie roczne PIT:
# przychody, koszty, PLN

# EUR -> PLN
# USD -> PLN
# PLN

# 1. wybór języka programowania
# 2. kodowanie = programowanie
# 3. testowanie = QA (Quality Assurance) = kontrola jakości

# Język programowania: Python  https://www.python.org/downloads/
# Edytora kodu (Word dla programistów): Visual Studio Code   https://code.visualstudio.com

# W terminalu:
# python program.py
# clear / cls
# pip install requests

# plik.py

# http://api.nbp.pl/api/exchangerates/rates/{table}/code}/{date}/
# http://api.nbp.pl/api/exchangerates/rates/a/usd/2023-05-08/?format=json

# A = kursów średnich
# B = kursów sprzedaży i zakupu

# dane = {
#     "table": "A",
#     "currency": "dolar amerykański",
#     "code": "USD",
#     "rates": [
#         {
#             "no": "087/A/NBP/2023",
#             "effectiveDate": "2023-05-08",
#             "mid": 4.1384
#         }
#     ]
# }

# 1. Przynieść skrzynkę z narzędziami do domu
# 2. Wyciągnąć wiertarkę ze skrzynki i położyć na stole
# 3. Użyc wiertarki





from requests import get

print("KALKULATOR WALUT")

waluta = input("Podaj walutę: ")

dzien = input("Podaj dzień (RRRR-MM-DD): ")

strona = get(f"http://api.nbp.pl/api/exchangerates/rates/a/{waluta}/{dzien}/?format=json")

dane = strona.json()

kurs = dane["rates"][0]["mid"]

print(f"1 {waluta} = {kurs} PLN w dniu {dzien}")