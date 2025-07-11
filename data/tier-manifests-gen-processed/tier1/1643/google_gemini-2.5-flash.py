def solve():
    """Index: 1643.
    Returns: the amount of money Valerie will have left over.
    """
    # L1
    num_small_bulbs = 3 # 3 small light bulbs
    cost_small_bulb = 8 # small light bulbs cost $8
    cost_small_bulbs_total = num_small_bulbs * cost_small_bulb

    # L2
    cost_large_bulb = 12 # large light bulbs cost $12
    total_cost_bulbs = cost_small_bulbs_total + cost_large_bulb

    # L3
    total_money_available = 60 # She has $60 to spend
    money_left_over = total_money_available - total_cost_bulbs

    # FA
    answer = money_left_over
    return answer