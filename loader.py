import pandas as pd
import json
import requests

url = 'https://finfo-api.vndirect.com.vn/v4/stock_prices?sort=date&size=1500&q=code:VCB~date:gte:2022-09-09'
agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'

headers = {'User-Agent': agent}

response = requests.get(url=url, headers=headers)
response_text = response.text
response_json = json.loads(response_text)
stock_data = pd.json_normalize(response_json['data'])
stock_data = stock_data.reset_index()

print(pd.json_normalize(response_json['data']))
