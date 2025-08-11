def solve():
    """Index: 542.
    Returns: the number of cans of frosting Bob needs to frost the remaining cakes.
    """
    # L1
    num_days = 5 # He does this for 5 days
    cakes_per_day = 10 # Sara bakes 10 cakes
    total_cakes_baked = num_days * cakes_per_day

    # L2
    carol_ate = 12 # eats 12 of his cakes
    cakes_remaining_after_carol = total_cakes_baked - carol_ate

    # L3
    cans_per_cake = 2 # 2 cans of frosting to frost a single cake
    cans_needed = cans_per_cake * cakes_remaining_after_carol

    # FA
    answer = cans_needed
    return answer