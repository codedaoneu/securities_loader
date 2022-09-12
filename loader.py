import pandas as pd
import json
from utils import *


class StockLoader:
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def query_generator(self, **kwargs):
        symbol_format = 'code:'
        symbol_query = ''
        from_date_query = '~date:gte:{0}'.format(self.start_date)
        to_date_query = '~date:lte:{0}'.format(self.end_date)
        base_query = from_date_query + to_date_query
        for key, value in kwargs.items():
            if key == 'symbol':
                symbol_query = symbol_format + value
        full_query = symbol_query + base_query
        return full_query

    def load_data_of_a_symbol(self, symbol):
        query = self.query_generator(start_date=self.start_date, end_date=self.end_date, symbol=symbol)
        res = get_response(query)
        json_res = json.loads(res.text)
        df = pd.json_normalize(json_res['data']).reset_index()
        return df
