def solve():
    """Index: 1177.
    Returns: the total amount James makes in a week from renting his car.
    """
    # L1
    hours_per_day = 8 # rents it for 8 hours a day
    days_per_week = 4 # 4 days a week
    total_hours = hours_per_day * days_per_week

    # L2
    rate_per_hour = 20 # $20 an hour
    total_earnings = total_hours * rate_per_hour

    # FA
    answer = total_earnings
    return answer