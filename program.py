# PLN
# USD -> PLN

# 1) wybór języka programowania
# 2) kodowanie = programowanie
# 3) testowanie = QA (Quality Assurance) = kontrola jakości

# W terminalu:
# python program.py
# clear / cls
# pip install requests

# http://api.nbp.pl/api/exchangerates/rates/{table}/{code}/today/
# http://api.nbp.pl/api/exchangerates/rates/a/usd/today/?format=json

# A = kurs śrendich
# B = kurs zakupu i sprzedaży

# 1. Wziąć skrzynkę z narzędziami (z wiertarką) z castoramy i przynieść do domu
# 2. Wyciągnąć ze skrzynki wiertarkę i położyć na biurku
# 3. Użyć wiertarki

dane = {
    "table": "A",
    "currency": "dolar amerykański",
    "code": "USD",
    "rates": [
        {
            "no": "113/A/NBP/2023",
            "effectiveDate": "2023-06-14",
            "mid": 4.1393
        }
    ]
}



from requests import get

print("KALKULATOR WALUT")

waluta = input("Podaj walutę: ")

dzien = input("Podaj dzień (RRRR-MM-DD): ")

strona = get(f"http://api.nbp.pl/api/exchangerates/rates/a/{waluta}/{dzien}/?format=json")

dane = strona.json()

kurs = dane["rates"][0]["mid"]

print(f"1 {waluta} = {kurs} PLN w dniu {dzien}")