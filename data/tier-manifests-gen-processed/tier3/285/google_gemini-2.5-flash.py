def solve():
    """Index: 285.
    Returns: the number of hours John has to watch a day.
    """
    # L1
    num_episodes = 20 # 20 episodes
    episode_length_minutes = 30 # each 30 minutes long
    total_minutes = num_episodes * episode_length_minutes

    # L2
    minutes_per_hour = 60 # WK
    total_hours = total_minutes / minutes_per_hour

    # L3
    num_days = 5 # in 5 days
    hours_per_day = total_hours / num_days

    # FA
    answer = hours_per_day
    return answer