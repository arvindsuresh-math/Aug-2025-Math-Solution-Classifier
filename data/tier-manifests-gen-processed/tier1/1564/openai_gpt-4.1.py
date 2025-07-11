def solve():
    """Index: 1564.
    Returns: the number of minutes Maddie watched over the weekend.
    """
    # L1
    total_episodes = 8 # Maddie watches 8 episodes
    episode_length = 44 # Each episode is about 44 minutes long
    total_minutes = total_episodes * episode_length

    # L2
    friday_episodes = 2 # she watches 2 episodes on Friday
    friday_minutes = friday_episodes * episode_length

    # L3
    monday_minutes = 138 # she watches 138 minutes of the show on Monday
    thursday_minutes = 21 # On Thursday, she watches 21 minutes
    weekday_minutes = monday_minutes + thursday_minutes + friday_minutes

    # L4
    weekend_minutes = total_minutes - weekday_minutes

    # FA
    answer = weekend_minutes
    return answer