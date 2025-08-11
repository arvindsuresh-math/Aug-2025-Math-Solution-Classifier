def solve():
    """Index: 7085.
    Returns: how much more money Classroom A needs to reach the goal.
    """
    # L1
    num_families_20 = 2 # 2 families
    amount_per_family_20 = 20 # $20 from each of two families
    raised_from_20_families = num_families_20 * amount_per_family_20

    # L2
    num_families_10 = 8 # eight families
    amount_per_family_10 = 10 # $10 from each of eight families
    raised_from_10_families = num_families_10 * amount_per_family_10

    # L3
    num_families_5 = 10 # ten families
    amount_per_family_5 = 5 # $5 from each of ten families
    raised_from_5_families = num_families_5 * amount_per_family_5

    # L4
    total_raised = raised_from_20_families + raised_from_10_families + raised_from_5_families

    # L5
    goal_amount = 200 # Each classroom must raise $200
    money_needed = goal_amount - total_raised

    # FA
    answer = money_needed
    return answer