def query_generator(start_date, end_date, **kwargs):
    symbol_format = 'code:'
    symbol_query = ''
    from_date_query = '~date:gte:{0}'.format(start_date)
    to_date_query = '~date:lte:{0}'.format(end_date)
    base_query = from_date_query + to_date_query
    for key, value in kwargs.items():
        if key == 'symbol':
            symbol_query = symbol_format + value
    full_query = symbol_query + base_query
    return full_query
