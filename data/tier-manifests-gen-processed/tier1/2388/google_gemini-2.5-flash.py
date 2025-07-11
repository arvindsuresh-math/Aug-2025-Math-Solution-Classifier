def solve():
    """Index: 2388.
    Returns: the total dollars Hank spent on fruits.
    """
    # L1
    num_dozens_bought = 14 # bought 14 dozen of each kind of fruit
    apples_cost_per_dozen = 40 # apples cost 40 dollars for a dozen
    cost_apples = num_dozens_bought * apples_cost_per_dozen

    # L2
    pears_cost_per_dozen = 50 # pears cost 50 dollars for a dozen
    cost_pears = pears_cost_per_dozen * num_dozens_bought

    # L3
    total_cost = cost_pears + cost_apples

    # FA
    answer = total_cost
    return answer