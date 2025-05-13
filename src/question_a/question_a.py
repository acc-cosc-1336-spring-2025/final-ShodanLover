# question_a.py

# write functions here, don't add input('') statements here!
def test_config():
    return True


class Stock:
    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name

    def get_symbol(self):
        return self.__symbol

    def get_company_name(self):
        return self.__company_name


def stock_purchase_history():
    stock1 = Stock("AAPL", "Apple Inc")
    stock2 = Stock("CAT", "Caterpillar")
    stock3 = Stock("EK", "Eastman Kodak")
    stock4 = Stock("GOOG", "Google")
    stock5 = Stock("MSFT", "Microsoft")

    stocks = {
        stock1.get_symbol(): stock1,
        stock2.get_symbol(): stock2,
        stock3.get_symbol(): stock3,
        stock4.get_symbol(): stock4,
        stock5.get_symbol(): stock5
    }

    print("\nStock Purchase History Report")
    print("{:<10}{}".format("Symbol", "Company Name"))
    print("-" * 30)
    for symbol, stock in stocks.items():
        print("{:<10}{}".format(stock.get_symbol(), stock.get_company_name()))
    print()
