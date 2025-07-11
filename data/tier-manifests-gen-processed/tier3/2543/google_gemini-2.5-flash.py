def solve():
    """Index: 2543.
    Returns: the number of times Matthew will fill his water bottle each week.
    """
    # L1
    glasses_per_day = 4 # Matthew drinks 4 glasses of water per day
    ounces_per_glass = 5 # Each glass is 5 ounces
    ounces_per_day = glasses_per_day * ounces_per_glass

    # L2
    days_per_week = 7 # WK
    ounces_per_week = days_per_week * ounces_per_day

    # L3
    bottle_capacity = 35 # a 35 ounces water bottle
    fills_per_week = ounces_per_week / bottle_capacity

    # FA
    answer = fills_per_week
    return answer