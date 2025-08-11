def solve():
    """Index: 3856.
    Returns: the total number of caps Lilith has collected.
    """
    # L1
    caps_per_month_first_year = 3 # 3 caps per month in the first year
    months_per_year = 12 # WK
    caps_first_year = caps_per_month_first_year * months_per_year

    # L2
    caps_per_month_after_first_year = 5 # 5 caps per month after the first year
    caps_per_year_after_first = caps_per_month_after_first_year * months_per_year

    # L3
    total_years_collecting = 5 # collecting for 5 years
    first_year_duration = 1 # implicit in "after the first year"
    years_after_first = total_years_collecting - first_year_duration

    # L4
    caps_after_first_period = caps_per_year_after_first * years_after_first

    # L5
    total_caps_collected_by_self = caps_first_year + caps_after_first_period

    # L6
    caps_from_christmas = 40 # receives 40 caps from friends and family
    total_caps_from_christmas = caps_from_christmas * total_years_collecting

    # L7
    caps_lost_per_year = 15 # loses 15 of the caps she has collected
    total_caps_lost = caps_lost_per_year * total_years_collecting

    # L8
    final_caps_collected = total_caps_collected_by_self + total_caps_from_christmas - total_caps_lost

    # FA
    answer = final_caps_collected
    return answer