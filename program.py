# PIT zeznanie roczne

# 1000 PLN
# 1000 USD => PLN

# 1) wybór języka programowania => Python
# 2) kodowanie = programowanie
# 3) testowanie = QA (Quality Assurance) = kontrola jakości

# Lewa strona = program = kartka papieru z przepisem kulinarnym
# Prawa strona = terminal = kuchnia z robotem kuchennym i ciastkami

# W terminalu:
# python program.py  # włączenie robota kuchennego
# clear  # wyczyść kuchnię
# pip install requests  # pójdź do Castoramy po wiertarkę

# Mario Bros / platformówka

# http://api.nbp.pl/api/exchangerates/rates/{table}/{code}/today/
# http://api.nbp.pl/api/exchangerates/rates/a/usd/today/?format=json

# A = kursy średnie
# B = kursów zakupu i sprzedaży

# 1. pójść do Castoramy po skrzynkę z narzędziami z wiertarką
# 2. wyciągnąć wiertarkę ze skrzynki i położyć ją na stole
# 3. używamy wiertarki

# from skrzynka import wiertarka

# dane = {
#     "table": "A",
#     "currency": "dolar amerykański",
#     "code": "USD",
#     "rates": [
#         {
#             "no": "156/A/NBP/2023",
#             "effectiveDate": "2023-08-14",
#             "mid": 4.0525
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
