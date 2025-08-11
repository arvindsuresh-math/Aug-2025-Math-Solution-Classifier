def solve():
    """Index: 4467.
    Returns: the total pounds of lettuce Julie bought.
    """
    # L1
    cost_green_lettuce = 8 # spends $8 on green lettuce
    cost_red_lettuce = 6 # $6 on red lettuce
    total_cost_lettuce = cost_green_lettuce + cost_red_lettuce

    # L2
    price_per_pound = 2 # $2 per pound
    total_pounds_lettuce = total_cost_lettuce / price_per_pound

    # FA
    answer = total_pounds_lettuce
    return answer