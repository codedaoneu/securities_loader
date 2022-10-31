import requests
from configparser import ConfigParser
import os


ABS_PATH = os.getcwd()
# get config
config = ConfigParser()
try:
    config.read(os.path.join(ABS_PATH, 'config.ini'))
    config.sections()
except Exception as e:
    print('config error')

BASE_URL = config['config']['BASE_URL']
url = config['config']['url']
agent = config['config']['agent']
sort = config['config']['sort']
size = config['config']['size']
page = config['config']['page']
# end get config


def get_response(query):
    params = {
        "sort": sort,
        "size": size,
        "page": page,
        "q": query
    }
    headers = {'User-Agent': agent}
    response = requests.get(url=BASE_URL, params=params, headers=headers)
    return response
