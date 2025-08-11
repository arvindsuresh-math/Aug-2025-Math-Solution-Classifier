def solve():
    """Index: 5657.
    Returns: the total number of mice the snake will eat in a decade.
    """
    # L1
    weeks_per_year = 52 # WK
    weeks_per_mouse = 4 # one mouse every 4 weeks
    mice_per_year = weeks_per_year / weeks_per_mouse

    # L2
    years_per_decade = 10 # WK
    mice_per_decade = mice_per_year * years_per_decade

    # FA
    answer = mice_per_decade
    return answer