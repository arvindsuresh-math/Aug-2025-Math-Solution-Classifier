def solve():
    """Index: 6194.
    Returns: the number of weeks it will take to watch the whole series.
    """
    # L1
    episodes_monday = 1 # 1 episode every Monday
    episodes_wednesday = 2 # 2 episodes every Wednesday
    episodes_per_week = episodes_monday + episodes_wednesday

    # L2
    total_episodes = 201 # There are 201 episodes
    weeks_to_watch = total_episodes / episodes_per_week

    # FA
    answer = weeks_to_watch
    return answer