def solve():
    """Index: 4875.
    Returns: the number of times Tony will fill his water bottle each week.
    """
    # L1
    water_per_day = 72 # 72 ounces of water per day
    days_per_week = 7 # WK
    water_per_week = water_per_day * days_per_week

    # L2
    bottle_capacity = 84 # an 84-ounce water bottle
    fills_per_week = water_per_week / bottle_capacity

    # FA
    answer = fills_per_week
    return answer