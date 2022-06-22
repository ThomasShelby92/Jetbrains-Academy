import requests


def get_rate(a,b):
    s = f'http://www.floatrates.com/daily/{a}.json'
    r = requests.get(s).json()
    b = b.lower()
    return r[b]["rate"]





cache = {}
currency = input()
if (currency != 'EUR' and currency != 'eur'):
    cache['eur'] = get_rate(currency,'EUR')
if (currency != 'USD' and currency !='usd'):
    cache['usd'] = get_rate(currency,'USD')

while True:
    found = 0
    exchange_code = input()
    if exchange_code == "":
        break
    amount = float(input())
    print("Checking the cache...")
    for i in cache:
        if exchange_code == i:
            print("Oh! It is in the cache!")
            print(f"You received {round((cache[i] * amount),2)} {exchange_code}.")
            found = 1
    if found == 0:
        print("Sorry, but it is not in the cache!")
        cache[exchange_code] = get_rate(currency, exchange_code)
        print(f"You received {round(amount * cache[exchange_code],2)} {exchange_code}.")


