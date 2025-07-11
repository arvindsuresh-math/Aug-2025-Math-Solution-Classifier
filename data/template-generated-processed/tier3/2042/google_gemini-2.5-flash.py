def solve():
    """Index: 2042.
    Returns: the amount of money the PTA had left.
    """
    # L1
    initial_money = 400 # The PTA had saved $400
    school_supplies_divisor = 4 # a fourth of the money
    school_supplies_cost = initial_money / school_supplies_divisor

    # Calculate the money left after spending on school supplies, which is used in L2 and L3.
    money_after_supplies = initial_money - school_supplies_cost

    # L2
    food_divisor = 2 # half of what was left
    food_cost = money_after_supplies / food_divisor

    # L3
    money_left = money_after_supplies - food_cost

    # FA
    answer = money_left
    return answer