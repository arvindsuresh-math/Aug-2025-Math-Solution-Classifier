def solve():
    """Index: 6854.
    Returns: the average number of episodes per year.
    """
    # L1
    seasons_group1 = 8 # 8 seasons had 15 episodes
    episodes_per_season_group1 = 15 # 15 episodes
    total_episodes_group1 = seasons_group1 * episodes_per_season_group1

    # L2
    seasons_group2 = 4 # 4 seasons had 20 episodes
    episodes_per_season_group2 = 20 # 20 episodes
    total_episodes_group2 = seasons_group2 * episodes_per_season_group2

    # L3
    seasons_group3 = 2 # 2 seasons had 12 episodes
    episodes_per_season_group3 = 12 # 12 episodes
    total_episodes_group3 = seasons_group3 * episodes_per_season_group3

    # L4
    total_all_episodes = total_episodes_group1 + total_episodes_group2 + total_episodes_group3

    # L5
    total_years = 14 # 14 years
    average_episodes_per_year = total_all_episodes / total_years

    # FA
    answer = average_episodes_per_year
    return answer