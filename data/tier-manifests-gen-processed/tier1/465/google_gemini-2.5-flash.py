def solve():
    """Index: 465.
    Returns: how much longer the first route will be if all 3 stoplights are red compared to the second route.
    """
    # L1
    time_route1_all_green = 10 # 10 minutes if all three lights are green
    num_stoplights_route1 = 3 # 3 stoplights
    time_added_per_red_light = 3 # each light that is red will add 3 minutes
    time_route1_all_red = time_route1_all_green + num_stoplights_route1 * time_added_per_red_light

    # L2
    time_route2 = 14 # takes 14 minutes
    time_difference = time_route1_all_red - time_route2

    # FA
    answer = time_difference
    return answer