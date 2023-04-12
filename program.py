# Język programowania: Python  https://www.python.org/downloads/
# Edytor kodu (Word dla programistów): Visual Studio Code  https://code.visualstudio.com

# Zeznanie roczne PIT

# PLN, EUR, USD
# USD -> PLN
# EUR -> PLN

# NASZ_PROGRAM  -> NBP:  Hej, jaki był kurs USD w dniu 2023-04-09?
# NBP -> NASZ_PROGRRAM: Tutaj był kurs ...

# 1) wybór języka programowania
# 2) kodowanie = programowanie
# 3) testowanie = QA (Quality Assurance) = kontrola jakości

# plik.py

# Język programowania
# 1. łatwy = prosty
# 2. łatwe znalezienie pracę (popularny, dużo ofert pracy, nie może być zbyt konkurencyjny)

# Trudne: C, C++, assembler
# Średnio-trudne: Java, C#
# Proste: Python, Javascript, Ruby, VBA

# W terminalu:
# python program.py
# clear
# pip install requests

# 1. Wziąć z Castoramy skrzynkę z narzędziami: pip install requests
# 2. Wyjąć wiertarkę ze skrzynki i położyć biurku
# 3. Użyć wiertarki

# from skrzynka import wiertarka

from requests import get

print("KALKULATOR WALUT")

waluta = input("Podaj walutę: ")

dzien = input("Podaj dzień (RRRR-MM-DD): ")

strona = get(f"http://api.nbp.pl/api/exchangerates/rates/a/{waluta}/{dzien}/?format=json")

dane = strona.json()

kurs = dane["rates"][0]["mid"]

print(f"1 {waluta} = {kurs} PLN w dniu {dzien}")

# flask Django

# http://api.nbp.pl/api/exchangerates/rates/{table}/{code}/{date}/
# http://api.nbp.pl/api/exchangerates/rates/a/usd/2023-04-12/?format=json

# A = kursów srednich
# B = kursó∑ zakupu i sprzedaży

# dane = {
#     "table": "A",
#     "currency": "dolar amerykański",
#     "code": "USD",
#     "rates": [
#         {
#             "no": "071/A/NBP/2023",
#             "effectiveDate": "2023-04-12",
#             "mid": 4.2713
#         }
#     ]
# }