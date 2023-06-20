# PLN
# USD -> PLN
# EUR -> PLN

# 1) wybór język programowania
# 2) programowanie = kodowanie
# 3) testowanie = QA (Quality Assurance) = kontrola jakości

# W terminalu:
# python program.py
# clear / cls

# http://api.nbp.pl/api/exchangerates/rates/{table}/{code}/today/
# http://api.nbp.pl/api/exchangerates/rates/a/usd/today/?format=json

# A = kursów średnich
# B = kursów zakupu i sprzedaży

# 1. Przynieść z castoramy skrzynkę z narzędziami (z wiertarką) do domu: pip install requests
# 2. Wyciągnąć wiertarkę ze skrzynki i położyć na biurku
# 3. Użyć wiertarki

# dane = {
#     "table": "A",
#     "currency": "dolar amerykański",
#     "code": "USD",
#     "rates": [
#         {
#             "no": "117/A/NBP/2023",
#             "effectiveDate": "2023-06-20",
#             "mid": 4.0580
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