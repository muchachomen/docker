import requests

data = {
    'name': 'kia',
    'country': 'Korea',
    'info': 'cool car'
}

response = requests.put("http://127.0.0.1:8000/api/cars/", json= data)
print(response.status_code)
print(response.text)