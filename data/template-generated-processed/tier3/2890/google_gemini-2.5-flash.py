def solve():
    """Index: 2890.
    Returns: the amount of money Kyle has left.
    """
    # L1
    dave_money = 46 # Dave has $46
    multiplier = 3 # 3 times what Dave has
    less_amount = 12 # $12 less than
    kyle_initial_money = dave_money * multiplier - less_amount

    # L2
    spending_divisor = 3 # a third of it
    snowboarding_cost = kyle_initial_money / spending_divisor

    # L3
    kyle_remaining_money = kyle_initial_money - snowboarding_cost

    # FA
    answer = kyle_remaining_money
    return answer