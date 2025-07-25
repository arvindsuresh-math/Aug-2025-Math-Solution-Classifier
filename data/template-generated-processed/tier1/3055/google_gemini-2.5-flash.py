def solve():
    """Index: 3055.
    Returns: the percentage of vinegar left after 2 years.
    """
    # L1
    initial_percent = 100 # WK
    evaporation_percent_per_year = 20 # 20% of the vinegar evaporates
    percent_left_after_one_year = initial_percent - evaporation_percent_per_year

    # L2
    percent_divisor = 100 # WK
    percent_left_after_two_years = (percent_left_after_one_year * percent_left_after_one_year) / percent_divisor

    # FA
    answer = percent_left_after_two_years
    return answer