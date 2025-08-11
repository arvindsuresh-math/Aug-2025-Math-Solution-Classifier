def solve():
    """Index: 159.
    Returns: the price of a haircut on Sunday.
    """
    # L1
    monday_price = 18 # $18 for his last haircut on Monday
    weekend_increase_percent = 50 # 50% more expensive
    percent_factor = 0.01 # WK
    increase_amount = monday_price * weekend_increase_percent * percent_factor

    # L2
    sunday_price = increase_amount + monday_price

    # FA
    answer = sunday_price
    return answer