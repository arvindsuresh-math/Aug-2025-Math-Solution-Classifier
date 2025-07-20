from fractions import Fraction

def solve():
    """Index: 6298.
    Returns: the number of days Marc needs to finish all episodes.
    """
    # L1
    total_episodes = 50 # 50 episodes of the show
    fraction_watched_per_day = Fraction(1, 10) # 1/10 of the episodes he bought
    episodes_per_day = total_episodes * fraction_watched_per_day

    # L2
    days_to_finish = total_episodes / episodes_per_day

    # FA
    answer = days_to_finish
    return answer