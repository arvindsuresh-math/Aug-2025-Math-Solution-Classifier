def solve():
    """Index: 843.
    Returns: the amount of money Randy has left.
    """
    # L1
    initial_money = 30 # Randy has $30
    lunch_cost = 10 # spent $10 buying his lunch
    money_after_lunch = initial_money - lunch_cost

    # L2
    quarter_divisor = 4 # a quarter of the money
    ice_cream_cost = money_after_lunch / quarter_divisor

    # L3
    money_left = money_after_lunch - ice_cream_cost

    # FA
    answer = money_left
    return answer