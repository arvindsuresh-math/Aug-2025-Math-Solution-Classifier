def solve():
    """Index: 203.
    Returns: the cost of each candy bar.
    """
    # L1
    num_soft_drinks = 2 # 2 soft drinks
    cost_per_soft_drink = 4 # $ 4 each
    cost_soft_drinks = num_soft_drinks * cost_per_soft_drink

    # L2
    total_spent = 28 # He spent a total of 28 dollars
    cost_candy_bars = total_spent - cost_soft_drinks

    # L3
    num_candy_bars = 5 # 5 candy bars
    cost_per_candy_bar = cost_candy_bars / num_candy_bars

    # FA
    answer = cost_per_candy_bar
    return answer