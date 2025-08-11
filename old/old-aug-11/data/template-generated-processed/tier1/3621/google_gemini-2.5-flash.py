def solve():
    """Index: 3621.
    Returns: the total money the boss spends paying all employees every month.
    """
    # L1
    fiona_hours_per_week = 40 # Fiona worked for 40 hours a week
    hourly_rate = 20 # paid $20 per hour
    fiona_weekly_earnings = fiona_hours_per_week * hourly_rate

    # L2
    weeks_per_month = 4 # WK
    fiona_monthly_earnings = fiona_weekly_earnings * weeks_per_month

    # L3
    john_hours_per_week = 30 # John for 30 hours
    john_weekly_earnings = john_hours_per_week * hourly_rate

    # L4
    john_monthly_earnings = john_weekly_earnings * weeks_per_month

    # L5
    jeremy_hours_per_week = 25 # Jeremy for 25 hours
    jeremy_weekly_earnings = jeremy_hours_per_week * hourly_rate

    # L6
    jeremy_monthly_earnings = jeremy_weekly_earnings * weeks_per_month

    # L7
    total_monthly_spend = fiona_monthly_earnings + john_monthly_earnings + jeremy_monthly_earnings

    # FA
    answer = total_monthly_spend
    return answer