def solve():
    """Index: 3934.
    Returns: the number of hours Janet spends at the gym on Friday.
    """
    # L1
    hours_monday = 1.5 # an hour and a half each day on Monday
    hours_wednesday = 1.5 # an hour and a half each day on Wednesday
    hours_mon_wed = hours_monday + hours_wednesday

    # L2
    total_weekly_hours = 5 # 5 hours a week
    hours_tue_fri = total_weekly_hours - hours_mon_wed

    # L3
    num_tue_fri_days = 2 # WK
    hours_friday = hours_tue_fri / num_tue_fri_days

    # FA
    answer = hours_friday
    return answer