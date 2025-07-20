def solve():
    """Index: 7360.
    Returns: the total number of golden apples Apollo has to pay for the entire year.
    """
    # L1
    apples_per_month_first_half = 3 # charged three golden apples for the first six months
    months_first_half = 6 # for the first six months
    cost_first_half = apples_per_month_first_half * months_first_half

    # L2
    multiplier_twice = 2 # demands twice as many golden apples as before
    cost_second_half = cost_first_half * multiplier_twice

    # L3
    total_cost_year = cost_first_half + cost_second_half

    # FA
    answer = total_cost_year
    return answer