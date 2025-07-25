def solve():
    """Index: 2542.
    Returns: the number of additional pots produced in the last hour compared to the first.
    """
    # L1
    minutes_per_hour = 60 # WK
    cold_production_time_per_pot = 6 # takes 6 minutes to produce each molded flower pot
    pots_first_hour = minutes_per_hour / cold_production_time_per_pot

    # L2
    warm_production_time_per_pot = 5 # takes only 5 minutes to produce each pot
    pots_last_hour = minutes_per_hour / warm_production_time_per_pot

    # L3
    additional_pots = pots_last_hour - pots_first_hour

    # FA
    answer = additional_pots
    return answer