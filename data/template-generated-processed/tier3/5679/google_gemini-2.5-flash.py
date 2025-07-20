def solve():
    """Index: 5679.
    Returns: the number of packages of string cheese Kelly will need.
    """
    # L1
    oldest_daily_cheese = 2 # Her oldest wants 2 every day
    days_per_week = 5 # 5 days per week
    oldest_weekly_cheese = oldest_daily_cheese * days_per_week

    # L2
    youngest_daily_cheese = 1 # her youngest will only eat 1
    youngest_weekly_cheese = youngest_daily_cheese * days_per_week

    # L3
    total_weekly_cheese = oldest_weekly_cheese + youngest_weekly_cheese

    # L4
    num_weeks = 4 # for 4 weeks
    total_cheese_needed = num_weeks * total_weekly_cheese

    # L5
    cheese_per_pack = 30 # 30 string cheeses per pack
    num_packages = total_cheese_needed / cheese_per_pack

    # FA
    answer = num_packages
    return answer