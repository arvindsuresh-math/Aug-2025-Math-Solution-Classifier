def solve():
    """Index: 5849.
    Returns: the total hours of the show Max watched.
    """
    # L1
    episode_duration_minutes = 30 # 2:00 pm to 2:30 pm so that is 30 minutes.

    # L2
    episodes_watched_per_week = 4 # misses the Friday episode
    total_minutes_watched = episode_duration_minutes * episodes_watched_per_week

    # L3
    minutes_per_hour = 60 # WK
    total_hours_watched = total_minutes_watched / minutes_per_hour

    # FA
    answer = total_hours_watched
    return answer