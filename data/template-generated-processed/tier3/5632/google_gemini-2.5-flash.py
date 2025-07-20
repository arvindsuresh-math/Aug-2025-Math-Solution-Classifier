def solve():
    """Index: 5632.
    Returns: the number of days it will take Tom to finish watching the show.
    """
    # L1
    minutes_per_episode = 20 # each one of which is 20 minutes long
    num_episodes = 90 # The show has 90 episodes
    total_minutes_to_watch = minutes_per_episode * num_episodes

    # L2
    minutes_per_hour = 60 # WK
    total_hours_to_watch = total_minutes_to_watch / minutes_per_hour

    # L3
    hours_per_day_watching = 2 # two hours a day
    days_to_finish = total_hours_to_watch / hours_per_day_watching

    # FA
    answer = days_to_finish
    return answer