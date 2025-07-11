def solve():
    """Index: 145.
    Returns: the total number of hours James watched TV.
    """
    # L1
    jeopardy_episodes = 2 # 2 episodes of Jeopardy
    jeopardy_duration_per_episode = 20 # Jeopardy is 20 minutes
    total_jeopardy_minutes = jeopardy_episodes * jeopardy_duration_per_episode

    # L2
    wheel_of_fortune_multiplier = 2 # Wheel of Fortune is twice as long
    wheel_of_fortune_duration_per_episode = wheel_of_fortune_multiplier * jeopardy_duration_per_episode

    # L3
    wheel_of_fortune_episodes = 2 # 2 episodes of Wheel of Fortune
    total_wheel_of_fortune_minutes = wheel_of_fortune_duration_per_episode * wheel_of_fortune_episodes

    # L4
    total_minutes_watched = total_jeopardy_minutes + total_wheel_of_fortune_minutes

    # L5
    minutes_per_hour = 60 # WK
    total_hours_watched = total_minutes_watched / minutes_per_hour

    # FA
    answer = total_hours_watched
    return answer