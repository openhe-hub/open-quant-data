import jqdatasdk

if __name__ == '__main__':
    jqdatasdk.auth('16602105188', 'A5f6e778dx')
    print(jqdatasdk.get_price("000001.XSHE", start_date="2022-07-01", end_date="2023-06-01"))
    print(jqdatasdk.get_account_info())

