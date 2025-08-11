def solve():
    """Index: 587.
    Returns: the total number of hours Jeff spends working in an entire week.
    """
    # L1
    weekend_catching_up_hours = 3 # he spends 3 hours every day catching up
    weekend_work_ratio = 3 # three times as many hours on the weekend catching up as he does working
    weekend_work_hours_per_day = weekend_catching_up_hours / weekend_work_ratio

    # L2
    weekday_work_ratio = 4 # spends four times as many hours working as he does catching up (weekdays)
    weekday_catching_up_hours = 3 # he spends 3 hours every day catching up
    weekday_work_hours_per_day = weekday_work_ratio * weekday_catching_up_hours

    # L3
    weekend_days = 2 # WK
    weekday_days = 5 # WK
    total_work_hours = weekend_days * weekend_work_hours_per_day + weekday_days * weekday_work_hours_per_day

    # FA
    answer = total_work_hours
    return answer