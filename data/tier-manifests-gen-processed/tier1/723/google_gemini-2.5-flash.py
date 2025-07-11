def solve():
    """Index: 723.
    Returns: the total number of bags of chips eaten.
    """
    # L1
    multiplier_after_dinner = 2 # twice as many
    bags_for_dinner = 1 # a bag of chips for dinner
    bags_after_dinner = multiplier_after_dinner * bags_for_dinner

    # L2
    total_bags = bags_after_dinner + bags_for_dinner

    # FA
    answer = total_bags
    return answer