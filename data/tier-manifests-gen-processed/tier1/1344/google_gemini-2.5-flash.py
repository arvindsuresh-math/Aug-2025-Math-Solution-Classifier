def solve():
    """Index: 1344.
    Returns: how much more money Jame makes per year in his new job than the old job.
    """
    # L1
    new_job_hourly_rate = 20 # $20 per hour
    new_job_hours_per_week = 40 # works 40 hours a week
    new_job_weekly_pay = new_job_hourly_rate * new_job_hours_per_week

    # L2
    old_job_hourly_rate = 16 # $16 an hour
    old_job_hours_per_week = 25 # 25 hours per week
    old_job_weekly_pay = old_job_hourly_rate * old_job_hours_per_week

    # L3
    weekly_raise = new_job_weekly_pay - old_job_weekly_pay

    # L4
    weeks_per_year = 52 # 52 weeks a year
    annual_raise = weekly_raise * weeks_per_year

    # FA
    answer = annual_raise
    return answer