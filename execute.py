from core.loader import StockLoader

if __name__ == "__main__":
    VCB = StockLoader('2022-01-09', '2022-09-09')
    # test function get data of a specific stock symbol
    data = VCB.load_data_of_a_symbol('VCB')
    print(data)
    industry = VCB._get_security_industry()
    print(industry)
    info = VCB._get_all_security_info()
    print(info)
    vcb_info = VCB.get_info_of_a_symbol("BCC")
    print(vcb_info)
    vn30 = VCB.get_vn30_symbol_info()
    print(vn30)
    hnx30 = VCB.get_hnx30_symbol_info()
    print(hnx30)
    industry_vcb = VCB.symbol_industry_searcher("VCB")
    print(industry_vcb)
    events = VCB._get_security_event("2022-09-07")
    print(events)