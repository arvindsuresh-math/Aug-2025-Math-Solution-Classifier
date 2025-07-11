def solve():
    """Index: 2740.
    Returns: John's profit from driving Uber after accounting for car depreciation.
    """
    # L1
    car_purchase_price = 18000 # car he bought for $18,000
    car_tradein_value = 6000 # he got $6,000 back
    depreciation = car_purchase_price - car_tradein_value

    # L2
    uber_income = 30000 # John made $30,000 doing Uber
    profit = uber_income - depreciation

    # FA
    answer = profit
    return answer