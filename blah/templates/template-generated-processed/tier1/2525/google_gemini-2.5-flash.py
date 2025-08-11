def solve():
    """Index: 2525.
    Returns: the number of yellow crayons.
    """
    # L2
    red_crayons = 14 # 14 red crayons
    blue_more_than_red = 5 # 5 more blue crayons than red crayons
    blue_crayons = blue_more_than_red + red_crayons

    # L3
    double_multiplier = 2 # double the blue crayons
    yellow_less_than_double_blue = 6 # 6 less yellow crayons than double the blue crayons
    yellow_crayons = (blue_crayons * double_multiplier) - yellow_less_than_double_blue

    # FA
    answer = yellow_crayons
    return answer