def solve():
    """Index: 1965.
    Returns: the number of turtle statues on the lawn at the end of four years.
    """
    # L1
    initial_statues = 4 # created 4 statues and placed them on her lawn
    quadruple = 4 # quadrupled the number of statues
    after_second_year = initial_statues * quadruple

    # L2
    added_third_year = 12 # added another 12 statues
    after_adding_third_year = after_second_year + added_third_year

    # L3
    broken_third_year = 3 # a hail storm broke 3 of the statues
    after_breaking_third_year = after_adding_third_year - broken_third_year

    # L4
    multiplier_fourth_year = 2 # twice as many new statues as had been broken the year before
    added_fourth_year = multiplier_fourth_year * broken_third_year

    # L5
    total_statues = after_breaking_third_year + added_fourth_year

    # FA
    answer = total_statues
    return answer