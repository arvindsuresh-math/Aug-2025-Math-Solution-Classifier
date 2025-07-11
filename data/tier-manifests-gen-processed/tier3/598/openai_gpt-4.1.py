def solve():
    """Index: 598.
    Returns: the number of cups per day Sarah needs to eat to meet her weekly minimum requirement.
    """
    # L1
    days_in_week = 7 # There are 7 days in a week
    daily_recommendation = 2 # 2 cups are recommended per day
    total_weekly_requirement = days_in_week * daily_recommendation

    # L2
    cups_already_eaten = 8 # Sarah has already eaten 8
    cups_left = total_weekly_requirement - cups_already_eaten

    # L3
    days_passed = 5 # Sunday through Thursday equals 5 days that have passed
    days_left = days_in_week - days_passed

    # L4
    cups_per_day_needed = cups_left / days_left

    # FA
    answer = cups_per_day_needed
    return answer