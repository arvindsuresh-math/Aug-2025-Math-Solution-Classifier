def solve():
    """Index: 314.
    Returns: the number of pages Berry has to read on Saturday to reach his goal.
    """
    # L1
    daily_average_goal = 50 # average of 50 pages a day
    days_in_week = 7 # WK
    total_pages_goal_week = days_in_week * daily_average_goal

    # L2
    pages_sunday = 43 # 43 pages on Sunday
    pages_monday = 65 # 65 pages on Monday
    pages_tuesday = 28 # 28 pages on Tuesday
    pages_thursday = 70 # 70 pages
    pages_friday = 56 # 56 pages
    total_pages_read_so_far = pages_sunday + pages_monday + pages_tuesday + pages_thursday + pages_friday

    # L3
    pages_for_saturday = total_pages_goal_week - total_pages_read_so_far

    # FA
    answer = pages_for_saturday
    return answer