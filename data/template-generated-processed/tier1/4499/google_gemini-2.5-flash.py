def solve():
    """Index: 4499.
    Returns: how much more money Maisy will earn at her new job.
    """
    # L1
    current_hours_per_week = 8 # 8 hours a week
    current_wage_per_hour = 10 # $10 per hour
    current_weekly_earnings = current_hours_per_week * current_wage_per_hour

    # L2
    new_hours_per_week = 4 # 4 hours a week
    new_wage_per_hour = 15 # $15 per hour
    new_job_wage_earnings = new_hours_per_week * new_wage_per_hour

    # L3
    bonus_per_week = 35 # additional bonus of $35 per week
    new_job_total_earnings = new_job_wage_earnings + bonus_per_week

    # L4
    earnings_difference = new_job_total_earnings - current_weekly_earnings

    # FA
    answer = earnings_difference
    return answer