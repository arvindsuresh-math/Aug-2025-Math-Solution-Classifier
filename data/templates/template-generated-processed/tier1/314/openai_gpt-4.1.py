def solve():
    """Index: 314.
    Returns: the number of pages Berry has to read on Saturday to reach his goal.
    """
    # L1
    days_in_week = 7 # WK
    target_avg_per_day = 50 # average of 50 pages a day
    total_goal = days_in_week * target_avg_per_day

    # L2
    sunday = 43 # 43 pages on Sunday
    monday = 65 # 65 pages on Monday
    tuesday = 28 # 28 pages on Tuesday
    thursday = 70 # 70 pages on Thursday
    friday = 56 # 56 pages on Friday
    total_read = sunday + monday + tuesday + thursday + friday

    # L3
    saturday_needed = total_goal - total_read

    # FA
    answer = saturday_needed
    return answer