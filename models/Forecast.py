class Forecast:

    def __init__(self, user, supp_code, year, month, price, vol) -> None:
        
        self.user = user
        self.year = year
        self.month = month
        self.supp_code = supp_code
        self.price = price
        self.vol = vol