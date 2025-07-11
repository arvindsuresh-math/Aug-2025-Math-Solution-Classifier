def solve():
    """Index: 1630.
    Returns: the total number of pairs of shoes the cobbler can mend in a week.
    """
    # L1
    mend_rate_per_hour = 3 # 3 pairs of shoes in an hour
    hours_mon_thu_per_day = 8 # works for 8 hours each day
    mended_per_day_mon_thu = mend_rate_per_hour * hours_mon_thu_per_day

    # L2
    num_days_mon_thu = 4 # WK
    total_mended_mon_thu = mended_per_day_mon_thu * num_days_mon_thu

    # L3
    friday_end_hour = 11 # from 8am to 11am
    friday_start_hour = 8 # from 8am to 11am
    hours_friday = friday_end_hour - friday_start_hour

    # L4
    total_mended_friday = mend_rate_per_hour * hours_friday

    # L5
    total_mended_week = total_mended_mon_thu + total_mended_friday

    # FA
    answer = total_mended_week
    return answer