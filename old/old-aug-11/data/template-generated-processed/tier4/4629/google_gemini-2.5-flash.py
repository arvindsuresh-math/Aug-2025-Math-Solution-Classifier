def solve():
    """Index: 4629.
    Returns: the cost of four bottles of mineral water.
    """
    # L1
    total_cost_3_bottles = 1.50 # €1.50
    num_bottles_bought = 3 # 3 bottles
    cost_per_bottle = total_cost_3_bottles / num_bottles_bought

    # L2
    num_bottles_desired = 4 # four bottles
    total_cost_4_bottles = cost_per_bottle * num_bottles_desired

    # FA
    answer = total_cost_4_bottles
    return answer