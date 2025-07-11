def solve():
    """Index: 948.
    Returns: the number of times Jason goes to the library in 4 weeks.
    """
    # L1
    jason_multiplier = 4 # Jason goes to the library 4 times more often
    william_visits_per_week = 2 # William goes 2 times per week to the library
    jason_visits_per_week = jason_multiplier * william_visits_per_week

    # L2
    num_weeks = 4 # in 4 weeks
    jason_total_visits = jason_visits_per_week * num_weeks

    # FA
    answer = jason_total_visits
    return answer