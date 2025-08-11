def solve():
    """Index: 423.
    Returns: the amount of money Mom has left.
    """
    # L1
    banana_cost_per_pack = 4 # 2 packs of bananas for €4 each
    pears_cost = 2 # pears for €2
    asparagus_cost = 6 # asparagus for €6
    chicken_cost = 11 # a chicken for €11
    total_cost = banana_cost_per_pack + banana_cost_per_pack + pears_cost + asparagus_cost + chicken_cost

    # L2
    initial_money = 55 # She left with €55
    money_left = initial_money - total_cost

    # FA
    answer = money_left
    return answer