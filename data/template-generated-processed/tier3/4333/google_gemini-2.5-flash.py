def solve():
    """Index: 4333.
    Returns: the total number of episodes.
    """
    # L1
    total_seasons = 10 # 10 seasons
    half_divisor = 2 # Half the number of shows
    half_seasons = total_seasons / half_divisor

    # L2
    episodes_per_season_first_half = 20 # 20 episodes per season for the first half of seasons
    episodes_first_half = half_seasons * episodes_per_season_first_half

    # L3
    episodes_per_season_second_half = 25 # 25 for the second half of the show
    episodes_second_half = half_seasons * episodes_per_season_second_half

    # L4
    total_episodes = episodes_first_half + episodes_second_half

    # FA
    answer = total_episodes
    return answer