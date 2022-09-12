import requests
from configparser import ConfigParser


# get config
config = ConfigParser()
config.read('config.ini')
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
