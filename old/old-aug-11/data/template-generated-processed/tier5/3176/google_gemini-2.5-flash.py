def solve():
    """Index: 3176.
    Returns: Freddy's age in years.
    """
    # L4
    total_age_sum = 35 # ages add up to 35
    rebecca_age_difference = 2 # two years older than Rebecca
    freddy_age_difference = 4 # four years younger than Freddy
    constant_term_in_equation = freddy_age_difference - rebecca_age_difference

    # L5
    three_times_matthew_age = total_age_sum - constant_term_in_equation

    # L6
    num_children = 3 # three children
    matthew_age = three_times_matthew_age / num_children

    # L7
    freddy_final_age = matthew_age + freddy_age_difference

    # FA
    answer = freddy_final_age
    return answer