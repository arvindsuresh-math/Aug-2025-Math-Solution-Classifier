def solve():
    """Index: 5085.
    Returns: the number of women living in Salem.
    """
    # L1
    salem_multiplier = 15 # Salem is 15 times the size of Leesburg
    leesburg_population = 58940 # Leesburg has 58940 people
    salem_initial_population = salem_multiplier * leesburg_population

    # L2
    people_moved_out = 130000 # 130000 people move out of Salem
    salem_current_population = salem_initial_population - people_moved_out

    # L3
    women_fraction_denominator = 2 # half of Salem's population is women
    women_in_salem = salem_current_population / women_fraction_denominator

    # FA
    answer = women_in_salem
    return answer