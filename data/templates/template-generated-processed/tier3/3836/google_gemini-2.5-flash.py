def solve():
    """Index: 3836.
    Returns: the cost of one of the remaining shirts.
    """
    # L1
    cost_per_shirt_first_group = 15 # 3 shirts that cost $15 each
    num_shirts_first_group = 3 # 3 shirts that cost $15 each
    cost_first_group = cost_per_shirt_first_group * num_shirts_first_group

    # L2
    total_shirts = 5 # Five shirts together
    remaining_shirts_count = total_shirts - num_shirts_first_group

    # L3
    total_cost_all_shirts = 85 # cost $85
    cost_remaining_shirts = total_cost_all_shirts - cost_first_group

    # L4
    cost_one_remaining_shirt = cost_remaining_shirts / remaining_shirts_count

    # FA
    answer = cost_one_remaining_shirt
    return answer