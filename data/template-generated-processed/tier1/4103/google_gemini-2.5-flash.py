def solve():
    """Index: 4103.
    Returns: the money Abraham spent on the box of laundry detergent.
    """
    # L1
    num_shower_gels = 4 # 4 shower gels
    cost_per_shower_gel = 4 # $4 each
    total_shower_gel_cost = num_shower_gels * cost_per_shower_gel

    # L2
    cost_toothpaste = 3 # a tube of toothpaste for $3
    total_gel_toothpaste_cost = total_shower_gel_cost + cost_toothpaste

    # L3
    initial_budget = 60 # budget of $60
    remaining_budget = 30 # $30 remaining in his budget
    total_spent = initial_budget - remaining_budget

    # L4
    cost_laundry_detergent = total_spent - total_gel_toothpaste_cost

    # FA
    answer = cost_laundry_detergent
    return answer