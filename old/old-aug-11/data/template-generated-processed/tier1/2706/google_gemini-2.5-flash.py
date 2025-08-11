def solve():
    """Index: 2706.
    Returns: the net distance the leaf has traveled down the sidewalk.
    """
    # L1
    forward_per_gust = 5 # For every five feet that a gust blows it forward
    num_gusts = 11 # after 11 gusts of wind
    total_forward_distance = forward_per_gust * num_gusts

    # L2
    backward_per_swirl = 2 # blows it back two feet
    total_backward_distance = backward_per_swirl * num_gusts

    # L3
    net_distance_traveled = total_forward_distance - total_backward_distance

    # FA
    answer = net_distance_traveled
    return answer