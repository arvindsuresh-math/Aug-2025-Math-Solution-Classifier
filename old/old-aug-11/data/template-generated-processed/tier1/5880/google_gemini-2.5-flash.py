def solve():
    """Index: 5880.
    Returns: the total number of crackers Nedy ate.
    """
    # L1
    crackers_per_day_mon_thu = 8 # 8 packs of crackers from Monday to Thursday
    num_days_mon_thu = 4 # from Monday to Thursday
    crackers_mon_thu = crackers_per_day_mon_thu * num_days_mon_thu

    # L2
    multiplier_friday = 2 # twice the amount on Friday
    crackers_friday = crackers_per_day_mon_thu * multiplier_friday

    # L3
    total_crackers = crackers_mon_thu + crackers_friday

    # FA
    answer = total_crackers
    return answer