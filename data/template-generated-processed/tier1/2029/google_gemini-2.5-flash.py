def solve():
    """Index: 2029.
    Returns: the number of bags of chips Emily should buy.
    """
    # L1
    jeremy_bags = 3 # Jeremy buys 3 bags of chips
    stacy_bags = 4 # Stacy buys 4 bags
    jeremy_stacy_total = jeremy_bags + stacy_bags

    # L2
    total_needed = 10 # 10 bags of chips total
    emily_bags = total_needed - jeremy_stacy_total

    # FA
    answer = emily_bags
    return answer