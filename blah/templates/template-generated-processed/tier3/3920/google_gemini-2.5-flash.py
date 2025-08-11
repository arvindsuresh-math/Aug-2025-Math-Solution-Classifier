def solve():
    """Index: 3920.
    Returns: the total number of alligators at the end of a year.
    """
    # L1
    months_in_year = 12 # WK
    doubling_period_months = 6 # doubles every six months
    num_doubling_periods = months_in_year / doubling_period_months

    # L2
    initial_alligators = 4 # 4 alligators
    doubling_factor = 2 # doubles
    alligators_after_first_doubling = initial_alligators * doubling_factor

    # L3
    final_alligators = alligators_after_first_doubling * doubling_factor

    # FA
    answer = final_alligators
    return answer