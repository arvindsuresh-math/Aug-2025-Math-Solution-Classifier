def solve():
    """Index: 1681.
    Returns: the total amount spent on car soap.
    """
    # L1
    washes_per_bottle = 4 # 4 times
    total_weeks = 20 # 20 weeks
    bottles_needed = total_weeks / washes_per_bottle

    # L2
    cost_per_bottle = 4.00 # $4.00
    total_cost = cost_per_bottle * bottles_needed

    # FA
    answer = total_cost
    return answer