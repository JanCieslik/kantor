from datetime import datetime
import requests
def get_date():
    date = datetime.now()
    current_date = date.strftime("%Y-%m-%d %H:%M:%S")
    return current_date
def file_writing(rate, amount, currency):
    text = f"\n|date: {get_date()} | currency: {currency} | rate: {rate} | amount: {amount}      | pln_value : {rate * amount}|"
    writing_file = open('history.txt', 'a', encoding='utf-8')
    writing_file.write(text)

def get_exchange_rate(currency):
    try:
        response = requests.get(f'http://api.nbp.pl/api/exchangerates/rates/C/{currency}/?format=json')
        data = response.json()
        return data['rates'][0]['ask']
    except Exception as e:
        print(e)
        return None