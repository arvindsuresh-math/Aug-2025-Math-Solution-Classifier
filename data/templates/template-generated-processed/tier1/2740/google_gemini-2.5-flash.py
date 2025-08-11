def solve():
    """Index: 2740.
    Returns: John's profit from driving Uber.
    """
    # L1
    car_cost_initial = 18000 # bought for $18,000
    car_trade_in_value = 6000 # got $6000 back
    car_depreciation = car_cost_initial - car_trade_in_value

    # L2
    uber_earnings = 30000 # made $30,000 doing Uber
    profit = uber_earnings - car_depreciation

    # FA
    answer = profit
    return answer