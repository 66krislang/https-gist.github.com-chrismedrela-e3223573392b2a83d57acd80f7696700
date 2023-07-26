# PIT roczny

# PLN
# USD -> PLN

# 1) wybór język programowania
# 2) programowanie = kodowanie
# 3) kontrola jakości = QA (Quality Assurance) = testowanie

# Po prawej stronie - w terminalu (kuchnii + robot):
# python program.py # uruchomienie programu = wypieczenia ciasta
# clear  # wyczyszczenie kuchni

# http://api.nbp.pl/api/exchangerates/rates/{table}/{code}/today/
# http://api.nbp.pl/api/exchangerates/rates/a/usd/today/?format=json

# A = kursów średnich
# B = kursów zakupu i sprzedaży

# 1. pójść do castoramy po skrzynkę z narzędziami z wiertarką
# 2. wyciągamy ze skrzynki wiertarkę i kładziemy na biurku
# 3. używamy wiertarki

# dane = {
#     "table": "A",
#     "currency": "dolar amerykański",
#     "code": "USD",
#     "rates": [
#         {
#             "no": "143/A/NBP/2023",
#             "effectiveDate": "2023-07-26",
#             "mid": 3.9949
#         }
#     ]
# }




from requests import get

print("KALKULATOR WALUT")

waluta = input("Podaj walutę: ")

strona = get(f"http://api.nbp.pl/api/exchangerates/rates/a/{waluta}/today/?format=json")

dane = strona.json()

kurs = dane["rates"][0]["mid"]

print(f"1 {waluta} = {kurs} pln")
