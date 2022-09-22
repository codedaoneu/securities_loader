import pandas as pd
import json
from utils import *
import requests
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')


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

    def _get_security_industry(self):
        res = requests.get(url="https://api-finfo.vndirect.com.vn/v4/industry_classification?q=industryLevel:2",
                           headers={'User-Agent': config['config']['agent']}
                           )
        json_res = json.loads(res.text)
        df = pd.json_normalize(json_res['data']).reset_index()
        return df

    def _get_all_security_info(self):
        """
        get all information of listed stock symbols on the market.
        """
        res = requests.get("https://api-finfo.vndirect.com.vn/v4/stocks?q=type:STOCK~status:LISTED&size=3000",
                           headers={'User-Agent': config['config']['agent']}
                           )
        json_res = json.loads(res.text)
        df = pd.json_normalize(json_res['data']).reset_index()
        return df

    def get_info_of_a_symbol(self, symbol):
        all_symbol_info = self._get_all_security_info()
        info_of_symbol = all_symbol_info[all_symbol_info["code"] == symbol].reset_index()
        del info_of_symbol["level_0"]
        del info_of_symbol["index"]
        return info_of_symbol

    def get_vn30_symbol_info(self):
        all_symbol_info = self._get_all_security_info()
        vn30_symbol_info = all_symbol_info[all_symbol_info["indexCode"] == "VN30"].reset_index()
        del vn30_symbol_info["level_0"]
        del vn30_symbol_info["index"]
        return vn30_symbol_info

    def get_hnx30_symbol_info(self):
        all_symbol_info = self._get_all_security_info()
        hnx30_symbol_info = all_symbol_info[all_symbol_info["indexCode"] == "HNX30"].reset_index()
        del hnx30_symbol_info["level_0"]
        del hnx30_symbol_info["index"]
        return hnx30_symbol_info

    def symbol_industry_searcher(self, symbol):
        all_security_industries = self._get_security_industry()
        info_of_symbol = all_security_industries[all_security_industries["codeList"].str.contains(symbol)].reset_index()
        del info_of_symbol["level_0"]
        del info_of_symbol["index"]
        del info_of_symbol["totalCount"]
        del info_of_symbol["codeList"]
        return info_of_symbol

    def _get_security_event(self, date):
        """
        get all event information of stock market in a day.
        date format: "yyyy-MM-dd" (ex: "2022-01-01")
        """
        res = requests.get("https://api-finfo.vndirect.com.vn/v4/events?q=disclosureDate:{0}~locale:VN&size=3000"
                           .format(date),
                           headers={'User-Agent': config['config']['agent']}
                           )
        json_res = json.loads(res.text)
        df = pd.json_normalize(json_res['data']).reset_index()
        df["date"] = date
        del df["index"]
        return df
