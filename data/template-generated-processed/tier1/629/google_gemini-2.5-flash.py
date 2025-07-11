def solve():
    """Index: 629.
    Returns: the total amount earned by the teacher.
    """
    # L1
    periods_per_day = 5 # 5 periods a day
    pay_per_period = 5 # $5 per period
    pay_per_day = periods_per_day * pay_per_period

    # L2
    work_days_per_month = 24 # works 24 days a month
    pay_per_month = pay_per_day * work_days_per_month

    # L3
    months_worked = 6 # working for 6 months now
    total_earned = pay_per_month * months_worked

    # FA
    answer = total_earned
    return answer