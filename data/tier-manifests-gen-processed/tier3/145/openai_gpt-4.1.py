def solve():
    """Index: 145.
    Returns: the total number of hours James watched TV.
    """
    # L1
    jeopardy_episodes = 2 # 2 episodes of Jeopardy
    jeopardy_minutes = 20 # Jeopardy is 20 minutes
    jeopardy_total_minutes = jeopardy_episodes * jeopardy_minutes

    # L2
    wheel_multiplier = 2 # Wheel of Fortune is twice as long
    wheel_minutes = wheel_multiplier * jeopardy_minutes

    # L3
    wheel_episodes = 2 # 2 episodes of Wheel of Fortune
    wheel_total_minutes = wheel_minutes * wheel_episodes

    # L4
    total_minutes = jeopardy_total_minutes + wheel_total_minutes

    # L5
    minutes_per_hour = 60 # WK
    total_hours = total_minutes / minutes_per_hour

    # FA
    answer = total_hours
    return answer