import requests
from pprint import pprint

data = {'name': 'Petr', 'surname': 'Petrov'}
url = 'https://httpbin.org/post'
# response = requests.get(url, params=data)
response = requests.post(url, data=data)
pprint(response.json())