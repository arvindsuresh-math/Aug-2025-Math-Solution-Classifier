def solve():
    """Index: 3849.
    Returns: the amount of money Randy had at first.
    """
    # L1
    ice_cream_cost = 5 # If the ice cream cone cost $5
    fraction_spent_on_ice_cream = 4 # a quarter of the money he had left
    money_left_after_lunch = ice_cream_cost * fraction_spent_on_ice_cream

    # L2
    lunch_cost = 10 # He spent $10 buying his lunch
    initial_money = money_left_after_lunch + lunch_cost

    # FA
    answer = initial_money
    return answer