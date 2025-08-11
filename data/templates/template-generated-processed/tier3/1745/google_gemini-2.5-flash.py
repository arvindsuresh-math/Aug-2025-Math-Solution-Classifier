def solve():
    """Index: 1745.
    Returns: the number of hours Mila needs to work to earn as much as Agnes in a month.
    """
    # L1
    agnes_hourly_rate = 15 # Agnes makes $15 an hour
    agnes_weekly_hours = 8 # Agnes works 8 hours each week
    agnes_weekly_salary = agnes_hourly_rate * agnes_weekly_hours

    # L2
    weeks_per_month = 4 # WK
    agnes_monthly_salary = agnes_weekly_salary * weeks_per_month

    # L3
    mila_hourly_rate = 10 # Mila makes $10 an hour
    mila_hours_needed = agnes_monthly_salary / mila_hourly_rate

    # FA
    answer = mila_hours_needed
    return answer