# PLN
# USD -> PLN  #
# EUR -> PLN  #

# 1. Wybór język programowania
# 2. Kodowanie = programowanie
# 3. Testowanie = QA (Quality Assurance) = kontrola jakość

# Język programowania:  https://www.python.org/downloads/
# Edytor kodu (Word dla programistów):  Visual Studio Code  https://code.visualstudio.com

# W terminalu:
# python program.py
# clear / cls
# pip install requests

# http://api.nbp.pl/api/exchangerates/rates/{table}/code}/{date}/
# http://api.nbp.pl/api/exchangerates/rates/a/usd/2023-05-15/?format=json

# A = kursy średnie
# B = kursy zakupu/sprzedaży

# 1. wziąć z Castoramy skrzynkę z narzędziami (m.in. z wiertarką)
# 2. wyciągnąć wiertarkę ze skrzynki i położyć na biurku
# 3. użyć wiertarki

# dane = {
#     "table": "A",
#     "currency": "dolar amerykański",
#     "code": "USD",
#     "rates": [
#         {
#             "no": "092/A/NBP/2023",
#             "effectiveDate": "2023-05-15",
#             "mid": 4.1490
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