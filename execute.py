import pandas as pd
import json
import requests
from configparser import ConfigParser
from loader import query_generator


config = ConfigParser()
config.read('config.ini')

# get config
BASE_URL = config['config']['BASE_URL']
url = config['config']['url']
agent = config['config']['agent']
sort = config['config']['sort']
size = config['config']['size']
page = config['config']['page']
# end get config

query = query_generator(start_date='2022-09-09', end_date='2022-09-09', symbol='VCB')
params = {
        "sort": sort,
        "size": size,
        "page": page,
        "q": query
        }
headers = {'User-Agent': agent}

response = requests.get(url=BASE_URL, params=params, headers=headers)
response_text = response.text
response_json = json.loads(response_text)
stock_data = pd.json_normalize(response_json['data'])
stock_data = stock_data.reset_index()

print(pd.json_normalize(response_json['data']))
