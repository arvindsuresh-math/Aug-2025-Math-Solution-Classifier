def solve():
    """Index: 285.
    Returns: the number of hours John has to watch per day.
    """
    # L1
    num_episodes = 20 # There are 20 episodes
    minutes_per_episode = 30 # they are each 30 minutes long
    total_minutes = num_episodes * minutes_per_episode

    # L2
    minutes_per_hour = 60 # WK
    total_hours = total_minutes / minutes_per_hour

    # L3
    num_days = 5 # John wants to finish a show in 5 days
    hours_per_day = total_hours / num_days

    # FA
    answer = hours_per_day
    return answer