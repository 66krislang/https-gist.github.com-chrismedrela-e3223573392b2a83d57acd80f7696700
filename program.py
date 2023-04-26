# Język programowania:  Python https://www.python.org/downloads/
# Edytor kodu (Word dla programistów):  Visual Studio Code https://code.visualstudio.com

# PLN EUR USD

# EUR -> PLN
# USD -> PLN

# W terminalu:
# python program.py
# clear / cls
# pip install requests

# 1) wybór języka programowania
# 2) programowanie = kodowanie
# 3) testowanie = QA (Quality Assurance) = kontrola jakości

# 1. pójść do Castoramy po skrzynkę z narzędziami (wiertarką)
# 2. wyciągnąć wiertarkę ze skrzynki i położyć na biurku
# 3. użyć wiertarki

# from skrzynka import wiertarka



from requests import get

print("KALKULATOR WALUT")

waluta = input("Podaj walutę: ")

dzien = input("Podaj dzień (RRRR-MM-DD): ")

strona = get(f"http://api.nbp.pl/api/exchangerates/rates/a/{waluta}/{dzien}/?format=json")

dane = strona.json()

kurs = dane['rates'][0]['mid']

print(f"1 {waluta} = {kurs} PLN w dniu {dzien}")




# http://api.nbp.pl/api/exchangerates/rates/{table}/code}/{date}/
# http://api.nbp.pl/api/exchangerates/rates/a/usd/2023-04-26/?format=json

# A = kursy średnich
# B = kursy zakupu i sprzedaży

# dane = {
#     "table": "A",
#     "currency": "dolar amerykański",
#     "code": "USD",
#     "rates": [
#         {
#             "no": "081/A/NBP/2023",
#             "effectiveDate": "2023-04-26",
#             "mid": 4.1557
#         }
#     ]
# }

# Plugin GPT: Genie  https://github.com/ai-genie/chatgpt-vscode