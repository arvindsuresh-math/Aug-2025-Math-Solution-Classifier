def solve():
    """Index: 5578.
    Returns: the number of days it will take for Willy to finish the entire series.
    """
    # L1
    num_seasons = 3 # 3 seasons
    episodes_per_season = 20 # each 20 episodes long
    total_episodes = num_seasons * episodes_per_season

    # L2
    episodes_per_day = 2 # watches 2 episodes a day
    days_to_finish = total_episodes / episodes_per_day

    # FA
    answer = days_to_finish
    return answer