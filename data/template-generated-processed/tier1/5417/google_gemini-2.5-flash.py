def solve():
    """Index: 5417.
    Returns: Mary's final weight in pounds.
    """
    # L1
    initial_weight = 99 # 99 pounds at the start
    dropped_initial = 12 # dropped a dozen pounds
    weight_after_initial_drop = initial_weight - dropped_initial

    # L2
    multiplier_twice = 2 # twice the weight
    weight_added_back = dropped_initial * multiplier_twice

    # L3
    weight_after_gain_back = weight_after_initial_drop + weight_added_back

    # L4
    multiplier_three_times = 3 # three times more weight
    weight_dropped_again = dropped_initial * multiplier_three_times

    # L5
    weight_after_second_drop = weight_after_gain_back - weight_dropped_again

    # L6
    half_dozen = 6 # half of a dozen pounds
    final_weight = weight_after_second_drop + half_dozen

    # FA
    answer = final_weight
    return answer