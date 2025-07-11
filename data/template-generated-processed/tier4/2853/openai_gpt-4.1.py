def solve():
    """Index: 2853.
    Returns: the number of hours it takes to film 4 weeks of episodes.
    """
    # L1
    episode_length = 20 # Each episode is 20 minutes long
    filming_extra_fraction = 0.5 # it takes 50% longer than that to film each episode
    filming_extra_time = episode_length * filming_extra_fraction

    # L2
    filming_time_per_episode = episode_length + filming_extra_time

    # L3
    episodes_per_week = 5 # Each week they show 5 episodes
    num_weeks = 4 # 4 weeks of episodes
    total_episodes = episodes_per_week * num_weeks

    # L4
    total_filming_minutes = total_episodes * filming_time_per_episode

    # L5
    minutes_per_hour = 60 # WK
    total_filming_hours = total_filming_minutes / minutes_per_hour

    # FA
    answer = total_filming_hours
    return answer