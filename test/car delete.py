import requests

response = requests.delete('http://127.0.0.1:8000/api/cars/')
print(response.status_code)
print(response.text)