def solve():
    """Index: 723.
    Returns: the total number of bags of chips John ate.
    """
    # L1
    bags_dinner = 1 # eats a bag of chips for dinner
    multiplier_after_dinner = 2 # eats twice as many after dinner
    bags_after_dinner = multiplier_after_dinner * bags_dinner

    # L2
    total_bags = bags_after_dinner + bags_dinner

    # FA
    answer = total_bags
    return answer