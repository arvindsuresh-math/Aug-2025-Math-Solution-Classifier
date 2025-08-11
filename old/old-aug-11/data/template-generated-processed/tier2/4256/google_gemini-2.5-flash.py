def solve():
    """Index: 4256.
    Returns: how much Tim makes a week.
    """
    # L1
    tasks_per_day = 100 # 100 tasks a day
    pay_per_task = 1.2 # They each pay $1.2
    daily_earnings = tasks_per_day * pay_per_task

    # L2
    work_days_per_week = 6 # works 6 days a week
    weekly_earnings = daily_earnings * work_days_per_week

    # FA
    answer = weekly_earnings
    return answer