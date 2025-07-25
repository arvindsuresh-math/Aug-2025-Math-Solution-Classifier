def solve():
    """Index: 6939.
    Returns: the total time it will take to watch all episodes.
    """
    # L1
    num_seasons_before_announcement = 9 # There were 9 seasons before the announcement
    episodes_per_regular_season = 22 # Each season is 22 episodes
    current_episodes = num_seasons_before_announcement * episodes_per_regular_season

    # L2
    extra_episodes_last_season = 4 # 4 episodes longer
    new_season_episodes = episodes_per_regular_season + extra_episodes_last_season

    # L3
    total_episodes = current_episodes + new_season_episodes

    # L4
    episode_duration_hours = 0.5 # each episode is .5 hours
    total_watch_time_hours = total_episodes * episode_duration_hours

    # FA
    answer = total_watch_time_hours
    return answer