def solve():
    """Index: 465.
    Returns: how much longer the first route will take than the second if all 3 stoplights are red.
    """
    # L1
    base_time_first_route = 10 # will take him 10 minutes if all three lights are green
    num_stoplights = 3 # includes 3 stoplights
    red_light_penalty = 3 # each light that is red will add 3 minutes
    time_first_route_all_red = base_time_first_route + num_stoplights * red_light_penalty

    # L2
    time_second_route = 14 # second route ... takes 14 minutes
    time_difference = time_first_route_all_red - time_second_route

    # FA
    answer = time_difference
    return answer