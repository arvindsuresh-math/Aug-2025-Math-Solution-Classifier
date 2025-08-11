def solve():
    """Index: 2853.
    Returns: the total hours it would take to film the episodes.
    """
    # L1
    episode_length_minutes = 20 # Each episode is 20 minutes long
    longer_filming_percentage = 0.5 # it takes 50% longer than that to film each episode
    extra_filming_minutes = episode_length_minutes * longer_filming_percentage

    # L2
    total_filming_minutes_per_episode = episode_length_minutes + extra_filming_minutes

    # L3
    episodes_per_week = 5 # Each week they show 5 episodes
    num_weeks = 4 # film 4 weeks of episodes
    total_episodes_to_film = episodes_per_week * num_weeks

    # L4
    total_filming_minutes = total_episodes_to_film * total_filming_minutes_per_episode

    # L5
    minutes_per_hour = 60 # WK
    total_filming_hours = total_filming_minutes / minutes_per_hour

    # FA
    answer = total_filming_hours
    return answer