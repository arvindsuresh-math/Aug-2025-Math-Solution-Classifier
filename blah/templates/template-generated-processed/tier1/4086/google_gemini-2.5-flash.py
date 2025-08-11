def solve():
    """Index: 4086.
    Returns: the number of dishes Sandrine washed.
    """
    # L1
    multiplier_bananas = 3 # 3 times the number of pears
    pears_picked = 50 # Charles picked 50 pears
    bananas_cooked = multiplier_bananas * pears_picked

    # L2
    dishes_more_than_bananas = 10 # 10 more than the number of bananas
    dishes_washed = bananas_cooked + dishes_more_than_bananas

    # FA
    answer = dishes_washed
    return answer