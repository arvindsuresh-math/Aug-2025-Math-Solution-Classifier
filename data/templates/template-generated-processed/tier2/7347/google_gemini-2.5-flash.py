def solve():
    """Index: 7347.
    Returns: the total hours of TV watched.
    """
    # L1
    short_show_episodes = 24 # The short show had 24 episodes
    short_show_duration_per_episode = 0.5 # a half-hour show per episode
    total_hours_short_show = short_show_episodes * short_show_duration_per_episode

    # L2
    long_show_episodes = 12 # the long show had 12 episodes
    long_show_duration_per_episode = 1 # a 1-hour long show per episode
    total_hours_long_show = long_show_episodes * long_show_duration_per_episode

    # L3
    total_hours_watched = total_hours_short_show + total_hours_long_show

    # FA
    answer = total_hours_watched
    return answer