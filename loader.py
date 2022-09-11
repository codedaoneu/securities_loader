import pandas as pd
import json
import requests

BASE_URL = 'https://finfo-api.vndirect.com.vn/v4/stock_prices/'
url = 'https://finfo-api.vndirect.com.vn/v4/stock_prices?sort=date&size=1500&q=code:VCB~date:gte:2022-09-09~date:lte:2022-09-09'
agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'

symbol = 'VCB'
start_date = '2022-09-09'
end_date = '2022-09-09'
query = 'code:{0}~date:gte:{1}~date:lte:{2}'.format(symbol, start_date, end_date)

print(query)
params = {
        "sort": "date",
        "size": 1500,
        "page": 1,
        "q": query
        }

headers = {'User-Agent': agent}

response = requests.get(url=BASE_URL, params=params, headers=headers)
response_text = response.text
response_json = json.loads(response_text)
stock_data = pd.json_normalize(response_json['data'])
stock_data = stock_data.reset_index()

print(pd.json_normalize(response_json['data']))
