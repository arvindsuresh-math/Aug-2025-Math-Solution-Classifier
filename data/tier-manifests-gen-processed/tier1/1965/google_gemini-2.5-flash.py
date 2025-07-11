def solve():
    """Index: 1965.
    Returns: the total number of turtle statues on the front lawn at the end of four years.
    """
    # L1
    initial_statues = 4 # 4 statues
    quadrupled_factor = 4 # quadrupled the number of statues
    statues_after_second_year = initial_statues * quadrupled_factor

    # L2
    added_third_year = 12 # added another 12 statues
    statues_before_broken = statues_after_second_year + added_third_year

    # L3
    broken_statues = 3 # broke 3 of the statues
    statues_after_broken = statues_before_broken - broken_statues

    # L4
    twice_factor = 2 # twice as many new statues
    added_fourth_year = twice_factor * broken_statues

    # L5
    final_statues = statues_after_broken + added_fourth_year

    # FA
    answer = final_statues
    return answer