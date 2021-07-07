import requests
import datetime
from datetime import date
from pprint import pprint

current_date = date.today()
past_date = current_date - datetime.timedelta(days=2)

url = 'https://api.stackexchange.com/2.3/questions'
params = {
    'fromdate': past_date,
    'order': 'desc',
    'sort': 'creation',
    'tagged': 'python',
    'site': 'stackoverflow'
}

response = requests.get(url, params=params)
response.raise_for_status()

pprint(response.json())