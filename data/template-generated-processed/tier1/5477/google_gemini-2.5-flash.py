def solve():
    """Index: 5477.
    Returns: the total money Regina would earn if she sold all the animals.
    """
    # L1
    cows = 20 # 20 cows
    pigs_per_cow_multiplier = 4 # four times more pigs
    num_pigs = pigs_per_cow_multiplier * cows

    # L2
    price_per_pig = 400 # $400 for each pig
    earnings_from_pigs = num_pigs * price_per_pig

    # L3
    price_per_cow = 800 # $800 for each cow
    earnings_from_cows = cows * price_per_cow

    # L4
    total_earnings = earnings_from_cows + earnings_from_pigs

    # FA
    answer = total_earnings
    return answer