def solve():
    """Index: 4733.
    Returns: the number of episodes Joe has to watch per day.
    """
    # L1
    num_seasons = 4 # 4 full seasons already aired
    episodes_per_season = 15 # each season has 15 episodes
    total_episodes = num_seasons * episodes_per_season

    # L2
    days_to_premiere = 10 # premiere in 10 days
    episodes_per_day = total_episodes / days_to_premiere

    # FA
    answer = episodes_per_day
    return answer