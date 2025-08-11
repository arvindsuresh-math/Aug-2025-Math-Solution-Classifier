def solve():
    """Index: 1564.
    Returns: how many more minutes she watched over the weekend.
    """
    # L1
    total_episodes_watched = 8 # 8 episodes of a TV show this week
    episode_length_minutes = 44 # Each episode is about 44 minutes long
    total_minutes_watched_week = total_episodes_watched * episode_length_minutes

    # L2
    friday_episodes = 2 # On Friday, she watches 2 episodes
    friday_minutes_watched = friday_episodes * episode_length_minutes

    # L3
    monday_minutes = 138 # 138 minutes of the show on Monday
    thursday_minutes = 21 # On Thursday, she watches 21 minutes
    total_minutes_weekday = monday_minutes + thursday_minutes + friday_minutes_watched

    # L4
    weekend_minutes_watched = total_minutes_watched_week - total_minutes_weekday

    # FA
    answer = weekend_minutes_watched
    return answer