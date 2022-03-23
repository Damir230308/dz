# Номер 2

import requests
from datetime import datetime

r = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text.split("</Valute>")
charcode = 'Доллар США'
charcode1 = 'Евро'
def currency_rates():
    for n in r:
        if n.count(charcode):
            nominal = (int(n[n.find('<Nominal>') + len('<Nominal>'):n.find('</Nominal>')]))
            value = (float(n[n.find('<Value>') + len('<Value>'):n.find('</Value>')].replace(',', '.')))
            result = (f"{nominal} {charcode} равен {value} рублей")
            for n in r:
                if n.count(charcode1):
                    nominal = (int(n[n.find('<Nominal>') + len('<Nominal>'):n.find('</Nominal>')]))
                    value = (float(n[n.find('<Value>') + len('<Value>'):n.find('</Value>')].replace(',', '.')))
                    result1 = (f"{nominal} {charcode1} равен {value} рублей")
                    date = datetime.now()
                    result2 = (f"{result} на {date}")
                    result3 = (f"{result1} на {date}")
                    print(result2)
                    print(result3)
currency_rates()
