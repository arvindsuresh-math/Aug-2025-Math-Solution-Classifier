def solve():
    """Index: 677.
    Returns: the amount of money Mr. Caiden is required to pay for the remaining metal roofing.
    """
    # L1
    required_feet = 300 # requires 300 feet of metal roofing
    free_feet = 250 # brings in 250 feet of metal roofing for free
    remaining_feet = required_feet - free_feet

    # L2
    cost_per_foot = 8 # each foot of roofing costs $8
    total_cost = remaining_feet * cost_per_foot

    # FA
    answer = total_cost
    return answer