from requests import post

url = 'http://localhost:8000/rate'

data = {
    'symbol_from': 'EUR',
    'symbol_to': 'JPY',
    'amoun_from': 25,
}

print(post(url=url, json=data).text)