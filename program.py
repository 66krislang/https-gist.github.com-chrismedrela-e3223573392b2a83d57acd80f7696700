# PLN
# EUR -> PLN
# USD -> PLN

# NBP

# 1) wybór języka programowania
# 2) programowanie = kodowanie
# 3) testowanie = QA (Quality Assurance) = kontrola jakości

# W terminalu:
# python program.py
# clear
# pip install requests

# http://api.nbp.pl/api/exchangerates/rates/{table}/{code}/today/
# http://api.nbp.pl/api/exchangerates/rates/a/usd/today/?format=json

# A = kurs średnich
# B = kurs sprzedaży i zakupu

# 1. pójdziemy do Castoramy po skrzynkę z narzędziami z wiertarką: pip install requests
# 2. wyciągamy wiertarkę ze skrzynki i kładziemy na biurku
# 3. używamy wiertarki

# dane = {
#     "table": "A",
#     "currency": "dolar amerykański",
#     "code": "USD",
#     "rates": [
#         {
#             "no": "128/A/NBP/2023",
#             "effectiveDate": "2023-07-05",
#             "mid": 4.0869
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
