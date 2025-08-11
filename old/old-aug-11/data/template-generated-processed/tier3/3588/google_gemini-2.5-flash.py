def solve():
    """Index: 3588.
    Returns: the initial number of bedbugs.
    """
    # L1
    final_bedbugs = 810 # After four days, there were 810 bedbugs
    growth_factor = 3 # Every day, the number of bedbugs would triple
    bedbugs_day_3 = final_bedbugs / growth_factor

    # L2
    bedbugs_day_2 = bedbugs_day_3 / growth_factor

    # L3
    initial_bedbugs = bedbugs_day_2 / growth_factor

    # FA
    answer = initial_bedbugs
    return answer