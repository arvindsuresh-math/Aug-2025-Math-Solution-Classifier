def solve():
    """Index: 587.
    Returns: the total hours Jeff spends working in an entire week.
    """
    # L1
    daily_catching_up_hours = 3 # 3 hours every day catching up
    weekend_catch_up_multiple = 3 # three times as many hours on the weekend catching up with his Facebook pals as he does working
    weekend_working_hours_per_day = daily_catching_up_hours / weekend_catch_up_multiple

    # L2
    weekday_work_multiple = 4 # four times as many hours working as he does catching up
    weekday_working_hours_per_day = weekday_work_multiple * daily_catching_up_hours

    # L3
    weekend_days = 2 # WK
    weekday_days = 5 # WK
    total_working_hours_per_week = weekend_days * weekend_working_hours_per_day + weekday_days * weekday_working_hours_per_day

    # FA
    answer = total_working_hours_per_week
    return answer