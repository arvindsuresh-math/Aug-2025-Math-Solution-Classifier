def solve():
    """Index: 6257.
    Returns: the total number of coffee bean bags used per week.
    """
    # L1
    morning_bags = 3 # 3 bags of coffee beans every morning
    afternoon_multiplier = 3 # triple that number in the afternoon
    afternoon_bags = morning_bags * afternoon_multiplier

    # L2
    evening_multiplier = 2 # twice the morning number in the evening
    evening_bags = morning_bags * evening_multiplier

    # L3
    daily_total_bags = morning_bags + afternoon_bags + evening_bags

    # L4
    days_in_week = 7 # WK
    weekly_total_bags = daily_total_bags * days_in_week

    # FA
    answer = weekly_total_bags
    return answer