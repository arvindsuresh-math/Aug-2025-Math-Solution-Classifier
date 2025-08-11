def solve():
    """Index: 1630.
    Returns: the number of pairs of shoes the cobbler can mend in a week.
    """
    # L1
    pairs_per_hour = 3 # can mend 3 pairs of shoes in an hour
    hours_per_day = 8 # works for 8 hours each day (Mon-Thu)
    mon_thu_daily = pairs_per_hour * hours_per_day

    # L2
    mon_thu_days = 4 # From Monday to Thursday
    mon_thu_total = mon_thu_daily * mon_thu_days

    # L3
    friday_end = 11 # works from 8am to 11am
    friday_start = 8 # works from 8am to 11am
    friday_hours = friday_end - friday_start

    # L4
    friday_total = pairs_per_hour * friday_hours

    # L5
    total_week = mon_thu_total + friday_total

    # FA
    answer = total_week
    return answer