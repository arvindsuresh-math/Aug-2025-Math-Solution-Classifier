def solve():
    """Index: 2063.
    Returns: the total distance the thrown Frisbees traveled.
    """
    # L1
    bess_throws_count = 4 # she does this 4 times
    bess_throw_distance = 20 # Bess can throw the Frisbee as far as 20 meters
    bess_out_distance = bess_throws_count * bess_throw_distance

    # L2
    double_factor = 2 # WK
    bess_total_distance = bess_out_distance * double_factor

    # L3
    holly_throws_count = 5 # she does this 5 times
    holly_throw_distance = 8 # Holly can only throw the Frisbee as far as 8 meters
    holly_total_distance = holly_throws_count * holly_throw_distance

    # L4
    total_distance_traveled = bess_total_distance + holly_total_distance

    # FA
    answer = total_distance_traveled
    return answer