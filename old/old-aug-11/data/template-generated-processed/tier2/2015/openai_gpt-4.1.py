def solve():
    """Index: 2015.
    Returns: the amount Mark has leftover per week after his raise and new expenses.
    """
    # L1
    old_hourly_wage = 40 # earned 40 dollars per hour
    raise_percent = 1.05 # 5% raise (multiply by 1.05)
    new_hourly_wage = old_hourly_wage * raise_percent

    # L2
    hours_per_day = 8 # works 8 hours per day
    daily_earnings = new_hourly_wage * hours_per_day

    # L3
    days_per_week = 5 # 5 days per week
    weekly_earnings = daily_earnings * days_per_week

    # L4
    old_weekly_bills = 600 # old bills used to be 600 dollars a week
    trainer_cost = 100 # add a hundred dollar a week personal trainer
    new_weekly_expenses = old_weekly_bills + trainer_cost

    # L5
    leftover = weekly_earnings - new_weekly_expenses

    # FA
    answer = leftover
    return answer