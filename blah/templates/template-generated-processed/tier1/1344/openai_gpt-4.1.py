def solve():
    """Index: 1344.
    Returns: how much more money Jame makes per year in his new job than the old job.
    """
    # L1
    new_hourly = 20 # $20 per hour
    new_hours_per_week = 40 # 40 hours a week
    new_weekly = new_hourly * new_hours_per_week

    # L2
    old_hourly = 16 # $16 an hour
    old_hours_per_week = 25 # 25 hours per week
    old_weekly = old_hourly * old_hours_per_week

    # L3
    weekly_raise = new_weekly - old_weekly

    # L4
    weeks_per_year = 52 # 52 weeks a year
    yearly_raise = weekly_raise * weeks_per_year

    # FA
    answer = yearly_raise
    return answer