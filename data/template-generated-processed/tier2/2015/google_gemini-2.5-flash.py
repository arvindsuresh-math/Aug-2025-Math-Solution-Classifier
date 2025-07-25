def solve():
    """Index: 2015.
    Returns: how much Mark has leftover a week.
    """
    # L1
    old_hourly_wage = 40 # earned 40 dollars per hour
    raise_factor = 1.05 # 5% raise
    new_hourly_wage = old_hourly_wage * raise_factor

    # L2
    hours_per_day = 8 # works 8 hours per day
    daily_earnings = new_hourly_wage * hours_per_day

    # L3
    days_per_week = 5 # for 5 days per week
    weekly_earnings = daily_earnings * days_per_week

    # L4
    old_weekly_bills = 600 # old bills used to be 600 dollars a week
    personal_trainer_cost = 100 # add a hundred dollar a week personal trainer
    total_weekly_expenses = old_weekly_bills + personal_trainer_cost

    # L5
    weekly_leftover = weekly_earnings - total_weekly_expenses

    # FA
    answer = weekly_leftover
    return answer