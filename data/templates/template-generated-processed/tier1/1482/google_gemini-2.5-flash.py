def solve():
    """Index: 1482.
    Returns: the total number of episodes Donna can watch in a week.
    """
    # L1
    episodes_per_weekday = 8 # 8 episodes each day during weekdays
    weekdays_in_week = 5 # WK
    episodes_weekdays = episodes_per_weekday * weekdays_in_week

    # L2
    weekend_multiplier = 3 # three times the number of episodes
    episodes_per_weekend_day = episodes_per_weekday * weekend_multiplier

    # L3
    weekend_days_in_week = 2 # WK
    total_episodes_weekend = episodes_per_weekend_day * weekend_days_in_week

    # L4
    total_episodes_week = episodes_weekdays + total_episodes_weekend

    # FA
    answer = total_episodes_week
    return answer