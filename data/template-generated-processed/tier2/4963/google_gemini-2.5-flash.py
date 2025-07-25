def solve():
    """Index: 4963.
    Returns: the total cost to produce all the episodes.
    """
    # L1
    first_season_episodes = 12 # The first season had 12 episodes
    cost_per_episode_season1 = 100000 # costs $100,000 per episode for the first season
    cost_season1 = first_season_episodes * cost_per_episode_season1

    # L2
    episode_increase_factor = 0.5 # 50% more episodes
    additional_episodes_per_season = first_season_episodes * episode_increase_factor

    # L3
    episodes_per_later_season = first_season_episodes + additional_episodes_per_season

    # L4
    num_middle_seasons = 3 # WK
    last_season_episodes = 24 # last season, which had 24 episodes
    total_episodes_later_seasons = episodes_per_later_season * num_middle_seasons + last_season_episodes

    # L5
    cost_multiplier_later_seasons = 2 # twice that much for every other season
    cost_per_episode_later_seasons = cost_multiplier_later_seasons * cost_per_episode_season1

    # L6
    total_cost_later_seasons = cost_per_episode_later_seasons * total_episodes_later_seasons

    # L7
    total_production_cost = total_cost_later_seasons + cost_season1

    # FA
    answer = total_production_cost
    return answer