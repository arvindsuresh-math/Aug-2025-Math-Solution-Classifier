def solve():
    """Index: 2083.
    Returns: the amount James spends on pistachios per week.
    """
    # L1
    cost_per_can = 10 # $10 per can
    ounces_per_can = 5 # Each can is 5 ounces
    cost_per_ounce = cost_per_can / ounces_per_can

    # L2
    ounces_eaten_per_period = 30 # He eats 30 ounces of pistachios
    days_in_period = 5 # every 5 days
    ounces_eaten_per_day = ounces_eaten_per_period / days_in_period

    # L3
    cost_per_day = ounces_eaten_per_day * cost_per_ounce

    # L4
    days_per_week = 7 # WK
    cost_per_week = cost_per_day * days_per_week

    # FA
    answer = cost_per_week
    return answer