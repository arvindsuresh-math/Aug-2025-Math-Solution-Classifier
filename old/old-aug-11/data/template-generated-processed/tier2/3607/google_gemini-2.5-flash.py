def solve():
    """Index: 3607.
    Returns: the total cost for fresh water for the day.
    """
    # L1
    family_members = 6 # family of 6
    water_per_person = 0.5 # 1/2 a gallon
    gallons_needed = family_members * water_per_person

    # L2
    cost_per_gallon = 1 # cost $1 to purify a gallon
    total_cost = gallons_needed * cost_per_gallon

    # FA
    answer = total_cost
    return answer