from fractions import Fraction

def solve():
    """Index: 6741.
    Returns: the number of episodes remaining for Cesar to finish the series.
    """
    # L1
    episodes_per_season = 20 # each season has 20 episodes
    num_seasons = 12 # 12 seasons
    total_episodes = episodes_per_season * num_seasons

    # L2
    fraction_watched = Fraction(1, 3) # watched 1/3 of the series
    episodes_watched = fraction_watched * total_episodes

    # L3
    episodes_remaining = total_episodes - episodes_watched

    # FA
    answer = episodes_remaining
    return answer