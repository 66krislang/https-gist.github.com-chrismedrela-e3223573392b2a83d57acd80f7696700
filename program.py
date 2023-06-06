# PLN
# USD -> PLN

# 1) wybrać język programowania
# 2) kodowania = programowania
# 3) testowanie = QA (Quality Assurance) = kontrola jakości

# Język programowania:  https://www.python.org/downloads/
# Edytor kodu (Word dla programistów):  Visual Studio Code   https://code.visualstudio.com

# W terminalu:
# python program.py
# clear / cls
# pip install requests

# dane = {
#     "table": "A",
#     "currency": "dolar amerykański",
#     "code": "USD",
#     "rates": [
#         {
#             "no": "108/A/NBP/2023",
#             "effectiveDate": "2023-06-06",
#             "mid": 4.1964
#         }
#     ]
# }

# http://api.nbp.pl/api/exchangerates/rates/{table}/{code}/today/
# http://api.nbp.pl/api/exchangerates/rates/a/usd/today/?format=json

# A = kurs średnich
# B = kurs sprzedaży/zakupu

# 1. pójść do Castoramy po skrzynkę z narzędziami (z wiertarką) i przynieść ją do domu: w terminalu: pip install requests
# 2. ze skrzynki wyciągnąć wiertarkę i położyć na stole
# 3. użyj wiertarki



from requests import get

print("KALKULATOR WALUT")

waluta = input("Podaj walutę: ")

strona = get(f"http://api.nbp.pl/api/exchangerates/rates/a/{waluta}/today/?format=json")

dane = strona.json()

kurs = dane["rates"][0]["mid"]

print(f"1 {waluta} = {kurs} PLN")