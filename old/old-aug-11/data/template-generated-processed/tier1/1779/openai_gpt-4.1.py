def solve():
    """Index: 1779.
    Returns: the total number of dreams Gavin has had in the two years.
    """
    # L1
    dreams_per_day = 4 # 4 dreams every day
    days_per_year = 365 # WK
    dreams_this_year = dreams_per_day * days_per_year

    # L2
    twice = 2 # twice as many dreams last year
    dreams_last_year = twice * dreams_this_year

    # L3
    total_dreams = dreams_last_year + dreams_this_year

    # FA
    answer = total_dreams
    return answer