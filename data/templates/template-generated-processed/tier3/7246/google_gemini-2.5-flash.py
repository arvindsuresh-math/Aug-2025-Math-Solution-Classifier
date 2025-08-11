def solve():
    """Index: 7246.
    Returns: the difference in prayer times between Pastor Paul and Pastor Bruce in a week.
    """
    # L1
    paul_daily_prayers = 20 # prays 20 times per day
    days_in_week_excluding_sunday = 6 # WK
    paul_prayers_weekday = paul_daily_prayers * days_in_week_excluding_sunday

    # L2
    paul_sunday_multiplier = 2 # prays twice as much
    paul_prayers_sunday = paul_sunday_multiplier * paul_daily_prayers

    # L3
    paul_total_weekly_prayers = paul_prayers_weekday + paul_prayers_sunday

    # L4
    bruce_weekday_divisor = 2 # prays half as much as Pastor Paul
    bruce_prayers_weekday = paul_prayers_weekday / bruce_weekday_divisor

    # L5
    bruce_sunday_multiplier = 2 # prays twice as much as Pastor Paul
    bruce_prayers_sunday = paul_prayers_sunday * bruce_sunday_multiplier

    # L6
    bruce_total_weekly_prayers = bruce_prayers_weekday + bruce_prayers_sunday

    # L7
    difference_in_prayers = paul_total_weekly_prayers - bruce_total_weekly_prayers

    # FA
    answer = difference_in_prayers
    return answer