def solve():
    """Index: 5552.
    Returns: the length of the fourth episode in minutes.
    """
    # L1
    episode1_duration = 58 # 58 minutes
    episode2_duration = 62 # 62 minutes
    episode3_duration = 65 # 65 minutes
    first_three_episodes_total_minutes = episode1_duration + episode2_duration + episode3_duration

    # L2
    total_hours = 4 # 4 hours
    minutes_per_hour = 60 # WK
    total_duration_minutes = total_hours * minutes_per_hour

    # L3
    fourth_episode_duration = total_duration_minutes - first_three_episodes_total_minutes

    # FA
    answer = fourth_episode_duration
    return answer