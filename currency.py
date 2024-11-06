import requests

def get_exchange_rate(currency_code: str):
    response = requests.get(f"https://api.nbp.pl/api/exchangerates/rates/a/{currency_code}/?format=json")
    if response.status_code == 200:
        rate_data = response.json()
        return rate_data['rates'][0]['mid']
    return None
