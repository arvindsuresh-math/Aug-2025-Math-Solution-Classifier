def solve():
    """Index: 1180.
    Returns: the total cost to feed everyone.
    """
    # L1
    num_family_members = 36 # 36 family members
    people_per_combo = 6 # feed 6 people
    num_combos = num_family_members / people_per_combo

    # L2
    cost_per_combo = 12.00 # $12.00
    total_cost = cost_per_combo * num_combos

    # FA
    answer = total_cost
    return answer