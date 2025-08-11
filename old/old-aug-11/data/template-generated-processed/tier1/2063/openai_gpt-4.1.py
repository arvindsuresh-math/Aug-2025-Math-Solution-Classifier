def solve():
    """Index: 2063.
    Returns: the total distance the thrown Frisbees have traveled.
    """
    # L1
    bess_throws = 4 # Bess throws the Frisbee 4 times
    bess_distance_per_throw = 20 # as far as 20 meters
    bess_out_distance = bess_throws * bess_distance_per_throw

    # L2
    bess_return_multiplier = 2 # throws it back to her original position (doubles the distance)
    bess_total_distance = bess_out_distance * bess_return_multiplier

    # L3
    holly_throws = 5 # Holly throws 5 times
    holly_distance_per_throw = 8 # as far as 8 meters
    holly_total_distance = holly_throws * holly_distance_per_throw

    # L4
    total_distance = bess_total_distance + holly_total_distance

    # FA
    answer = total_distance
    return answer