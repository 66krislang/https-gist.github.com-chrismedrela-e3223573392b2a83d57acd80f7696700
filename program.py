# Python  https://www.python.org/downloads/
# Visual Studio Code  https://code.visualstudio.com
# W zakładce "extensions" zainstalować plugin do Pythona
# W terminalu: pip install requests

# Crash Course z Visual Studio Code:
# 1) boczny panel
# 2) edytor kodu
# 3) terminal

# nazwa_funkcji(argument1, argument2)
# zmienna.nazwa_metody(argument1, argument2)

# paczka = {
#     'imie': 'jan',
#     'nazwisko': 'kowalski',
# }
# print(paczka)
# print(paczka['imie'])

# lista = ["ala", "wojtek", "alina"]
# print(lista)
# print(lista[1])  # ==> wojtek

# osoby = [
#     {'imie': 'jan', 'nazwisko': 'kowalski'},
#     {'imie': 'ala', 'nazwisko': 'wisniewska'},
# ]

# print(osoby[1]['nazwisko'])  # ==> wisniewska

# dane = {
#     "table": "A",
#     "currency": "dolar amerykański",
#     "code": "USD",
#     "rates": [
#         {
#             "no": "159/A/NBP/2022",
#             "effectiveDate": "2022-08-18",
#             "mid": 4.6468
#         }
#     ]
# }

from requests import get

waluta = input("Podaj walutę: ")
waluta = waluta.upper()
data = input("Podaj datę: ")

odpowiedz = get(f"http://api.nbp.pl/api/exchangerates/rates/a/{waluta}/{data}/?format=json")

if odpowiedz.ok:
    dane = odpowiedz.json()
    kurs_waluty = dane['rates'][0]['mid']
    print(f"1 {waluta} = {kurs_waluty} PLN w dniu {data}")

    # http://api.nbp.pl/api/exchangerates/rates/a/usd/2022-08-18/?format=json

else:
    print("Brak danych")

print("Koniec")