def solve():
    """Index: 3448.
    Returns: the number of days Barney will not have clean towels.
    """
    # L1
    towels_per_day = 2 # uses two at a time that he changes to clean towels daily
    days_per_week = 7 # WK
    towels_per_week = towels_per_day * days_per_week

    # L2
    weeks_missed_plus_current = 2 # missed one week of laundry
    towels_needed_for_two_weeks = weeks_missed_plus_current * towels_per_week

    # L3
    towels_owned = 18 # He owns eighteen towels
    towels_short = towels_needed_for_two_weeks - towels_owned

    # L4
    days_without_clean_towels = towels_short / towels_per_day

    # FA
    answer = days_without_clean_towels
    return answer