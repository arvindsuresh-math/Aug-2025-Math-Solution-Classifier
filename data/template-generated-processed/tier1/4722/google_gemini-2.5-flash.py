def solve():
    """Index: 4722.
    Returns: the total number of ribbons Jane uses.
    """
    # L1
    dresses_per_day_initial = 2 # 2 dresses a day
    days_initial = 7 # 7 days
    dresses_first_period = dresses_per_day_initial * days_initial

    # L2
    dresses_per_day_next = 3 # 3 dresses a day
    days_next = 2 # next 2 days
    dresses_second_period = dresses_per_day_next * days_next

    # L3
    total_dresses = dresses_first_period + dresses_second_period

    # L4
    ribbons_per_dress = 2 # 2 ribbons to each dress
    total_ribbons = total_dresses * ribbons_per_dress

    # FA
    answer = total_ribbons
    return answer