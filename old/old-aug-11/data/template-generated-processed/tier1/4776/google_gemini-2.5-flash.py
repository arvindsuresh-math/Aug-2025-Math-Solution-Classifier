def solve():
    """Index: 4776.
    Returns: the total number of people at the fair in the three years.
    """
    # L1
    people_this_year = 600 # the number of people going to the fair this year is 600
    multiplier_next_year = 2 # twice as many people going to the fair
    people_next_year = multiplier_next_year * people_this_year

    # L2
    total_this_and_next_year = people_next_year + people_this_year

    # L3
    less_than_next_year_last_year = 200 # 200 less than those going next year
    people_last_year = people_next_year - less_than_next_year_last_year

    # L4
    total_three_years = total_this_and_next_year + people_last_year

    # FA
    answer = total_three_years
    return answer