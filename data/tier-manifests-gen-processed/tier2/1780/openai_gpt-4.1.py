def solve():
    """Index: 1780.
    Returns: the total amount Faith will earn by the end of the week.
    """
    # L1
    hourly_wage = 13.5 # $13.50 per hour
    regular_hours_per_day = 8 # 8 hours a day
    daily_regular_pay = hourly_wage * regular_hours_per_day

    # L2
    work_days_per_week = 5 # 5 days a week
    weekly_regular_pay = work_days_per_week * daily_regular_pay

    # L3
    overtime_hours_per_day = 2 # 2 hours of overtime per day
    daily_overtime_pay = overtime_hours_per_day * hourly_wage

    # L4
    weekly_overtime_pay = daily_overtime_pay * work_days_per_week

    # L5
    total_weekly_pay = weekly_regular_pay + weekly_overtime_pay

    # FA
    answer = total_weekly_pay
    return answer