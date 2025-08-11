def solve():
    """Index: 7382.
    Returns: the number of steaks Tommy needs to buy.
    """
    # L1
    num_family_members = 5 # 5 of them in total
    ounces_per_pound = 16 # each member wants one pound
    total_ounces_needed = num_family_members * ounces_per_pound

    # L2
    ounces_per_steak = 20 # the steaks are 20 ounces each
    num_steaks_needed = total_ounces_needed / ounces_per_steak

    # FA
    answer = num_steaks_needed
    return answer