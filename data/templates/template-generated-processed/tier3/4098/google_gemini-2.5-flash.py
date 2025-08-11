def solve():
    """Index: 4098.
    Returns: the number of ounces of coffee she now drinks a week.
    """
    # L2
    thermos_capacity = 20 # 20-ounce thermos
    milk_ounces_per_half_cup = 4 # WK
    coffee_per_thermos = thermos_capacity - milk_ounces_per_half_cup

    # L3
    times_per_day = 2 # twice a day
    ounces_per_day = times_per_day * coffee_per_thermos

    # L4
    school_days_per_week = 5 # five-day school week
    normal_weekly_ounces = ounces_per_day * school_days_per_week

    # L5
    reduction_divisor = 4 # 1/4 of what she normally drinks
    reduced_weekly_ounces = normal_weekly_ounces / reduction_divisor

    # FA
    answer = reduced_weekly_ounces
    return answer