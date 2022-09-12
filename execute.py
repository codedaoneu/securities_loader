from loader import StockLoader

if __name__ == "__main__":
    VCB = StockLoader('2022-01-09', '2022-09-09')
    # test function get data of a specific stock symbol
    data = VCB.load_data_of_a_symbol('VCB')
    print(data)
