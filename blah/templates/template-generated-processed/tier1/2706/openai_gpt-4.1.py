def solve():
    """Index: 2706.
    Returns: the number of feet the leaf has traveled down the sidewalk after 11 gusts of wind.
    """
    # L1
    feet_per_gust = 5 # gust blows it forward 5 feet
    num_gusts = 11 # after 11 gusts of wind
    total_forward = feet_per_gust * num_gusts

    # L2
    feet_per_swirl = 2 # wind swirls and blows it back two feet
    total_backward = feet_per_swirl * num_gusts

    # L3
    net_distance = total_forward - total_backward

    # FA
    answer = net_distance
    return answer