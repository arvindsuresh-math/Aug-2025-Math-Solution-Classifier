def solve():
    """Index: 542.
    Returns: the number of cans of frosting needed to frost the remaining cakes.
    """
    # L1
    days_baked = 5 # He does this for 5 days
    cakes_per_day = 10 # Sara bakes 10 cakes
    total_cakes = days_baked * cakes_per_day

    # L2
    cakes_eaten = 12 # Carol then comes over and eats 12 of his cakes
    cakes_remaining = total_cakes - cakes_eaten

    # L3
    cans_per_cake = 2 # it takes 2 cans of frosting to frost a single cake
    cans_needed = cans_per_cake * cakes_remaining

    # FA
    answer = cans_needed
    return answer