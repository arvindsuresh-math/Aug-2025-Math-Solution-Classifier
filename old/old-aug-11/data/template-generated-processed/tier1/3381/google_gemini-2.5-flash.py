def solve():
    """Index: 3381.
    Returns: the total cost of all 5 shirts.
    """
    # L1
    num_shirts_first_group = 3 # 3 shirts
    cost_per_shirt_first_group = 15 # $15 each
    cost_first_group = cost_per_shirt_first_group * num_shirts_first_group

    # L2
    total_shirts = 5 # 5 shirts
    remaining_shirts = total_shirts - num_shirts_first_group

    # L3
    cost_per_shirt_remaining = 20 # $20 each
    cost_remaining_shirts = cost_per_shirt_remaining * remaining_shirts

    # L4
    total_cost = cost_first_group + cost_remaining_shirts

    # FA
    answer = total_cost
    return answer