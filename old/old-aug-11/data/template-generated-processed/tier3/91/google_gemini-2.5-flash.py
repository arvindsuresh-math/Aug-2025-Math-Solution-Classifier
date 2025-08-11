def solve():
    """Index: 91.
    Returns: John's hourly rate if he earns the bonus.
    """
    # L1
    regular_workday_hours = 8 # works for 8 hours
    extra_work_hours = 2 # 2-hour longer workday
    bonus_workday_hours = regular_workday_hours + extra_work_hours

    # L2
    regular_daily_pay = 80 # makes $80 a day
    performance_bonus = 20 # extra $20 a day
    total_daily_pay_with_bonus = regular_daily_pay + performance_bonus

    # L3
    hourly_rate_with_bonus = total_daily_pay_with_bonus / bonus_workday_hours

    # FA
    answer = hourly_rate_with_bonus
    return answer