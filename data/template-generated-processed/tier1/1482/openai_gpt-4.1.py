def solve():
    """Index: 1482.
    Returns: the total number of episodes Donna can watch in a week.
    """
    # L1
    episodes_per_weekday = 8 # Donna can watch 8 episodes each day during weekdays
    num_weekdays = 5 # WK (Monday to Friday)
    weekday_total = episodes_per_weekday * num_weekdays

    # L2
    weekend_multiplier = 3 # three times the number of episodes on the weekdays
    episodes_per_weekend_day = episodes_per_weekday * weekend_multiplier

    # L3
    num_weekend_days = 2 # WK (Saturday and Sunday)
    weekend_total = episodes_per_weekend_day * num_weekend_days

    # L4
    total_episodes = weekday_total + weekend_total

    # FA
    answer = total_episodes
    return answer