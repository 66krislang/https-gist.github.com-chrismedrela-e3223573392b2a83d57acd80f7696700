# PLN
# USD -> PLN
# EUR -> PLN

# Skąd weźmiemy kursy => NBP

# 1) wybór języka programowania
# 2) programowanie = kodowanie
# 3) testowanie = Quality Assurance (QA) = kontrola jakości

# Visual Studio Code

# po lewej = przepis kulinarny (kartka)
# po prawej = kuchnia z robotem kuchennym

# W terminalu (po prawej):
# uruchamiamy robota: python program.py
# posprzątać kuchnię: clear

# http://api.nbp.pl/api/exchangerates/rates/{table}/{code}/today/
# http://api.nbp.pl/api/exchangerates/rates/a/usd/today/?format=json

# A = kursy średnie
# B = kursy zakupu i sprzedaży

# 1. pójść do castoramy po skrzynkę z narzędziami (z wiertarką): pip install requests
# 2. wyciągnąć wiertarkę ze skrzynki i położyć na biurku
# 3. użyć wiertarki

# dane = {
#     "table": "A",
#     "currency": "dolar amerykański",
#     "code": "USD",
#     "rates": [
#         {
#             "no": "138/A/NBP/2023",
#             "effectiveDate": "2023-07-19",
#             "mid": 3.9612
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
