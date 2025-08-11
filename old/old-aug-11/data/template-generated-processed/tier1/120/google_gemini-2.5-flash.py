def solve():
    """Index: 120.
    Returns: the amount of money Carrie will have left over after buying her bike.
    """
    # L1
    hourly_rate = 8 # $8 an hour
    hours_per_week = 35 # 35 hours a week
    weekly_earnings = hourly_rate * hours_per_week

    # L2
    weeks_per_month = 4 # WK
    monthly_earnings = weekly_earnings * weeks_per_month

    # L3
    bike_cost = 400 # bike for $400
    money_left_over = monthly_earnings - bike_cost

    # FA
    answer = money_left_over
    return answer