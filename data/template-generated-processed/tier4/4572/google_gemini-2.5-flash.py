def solve():
    """Index: 4572.
    Returns: the total fluid Jon drinks in a week in ounces.
    """
    # L1
    awake_hours = 16 # 16 hours he is awake
    drinking_interval_hours = 4 # every 4 hours
    small_bottles_per_day = awake_hours / drinking_interval_hours

    # L2
    small_bottle_size_ounces = 16 # 16 ounces
    ounces_from_small_bottles = small_bottles_per_day * small_bottle_size_ounces

    # L3
    large_bottle_percent_larger = 0.25 # 25% larger
    larger_bottle_extra_ounces = small_bottle_size_ounces * large_bottle_percent_larger

    # L4
    large_bottle_size_ounces = small_bottle_size_ounces + larger_bottle_extra_ounces

    # L5
    large_bottles_per_day = 2 # Twice a day
    ounces_from_large_bottles = large_bottle_size_ounces * large_bottles_per_day

    # L6
    total_ounces_per_day = ounces_from_small_bottles + ounces_from_large_bottles

    # L7
    days_per_week = 7 # WK
    total_ounces_per_week = total_ounces_per_day * days_per_week

    # FA
    answer = total_ounces_per_week
    return answer