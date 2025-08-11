def solve():
    """Index: 6458.
    Returns: the total amount Frank paid for his breakfast shopping.
    """
    # L1
    num_buns = 10 # 10 buns
    cost_per_bun = 0.1 # $0.1 each
    cost_buns = num_buns * cost_per_bun

    # L2
    num_milk_bottles = 2 # two bottles of milk
    cost_per_milk_bottle = 2 # $2 each
    cost_milk = num_milk_bottles * cost_per_milk_bottle

    # L3
    times_more_expensive = 3 # three times more expensive
    cost_eggs = times_more_expensive * cost_per_milk_bottle

    # L4
    total_cost = cost_buns + cost_milk + cost_eggs

    # FA
    answer = total_cost
    return answer