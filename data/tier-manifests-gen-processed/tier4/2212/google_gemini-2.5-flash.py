def solve():
    """Index: 2212.
    Returns: the total cost of the entire season.
    """
    # L1
    total_episodes = 22 # 22 episodes
    half_season_divisor = 2 # first half of the season
    episodes_per_half = total_episodes / half_season_divisor

    # L2
    cost_per_episode_first_half = 1000 # $1000 per episode
    cost_first_half = episodes_per_half * cost_per_episode_first_half

    # L3
    cost_increase_multiplier = 1.2 # 120% more expensive
    cost_increase_per_episode = cost_per_episode_first_half * cost_increase_multiplier

    # L4
    cost_per_episode_second_half = cost_per_episode_first_half + cost_increase_per_episode

    # L5
    cost_second_half = cost_per_episode_second_half * episodes_per_half

    # L6
    total_season_cost = cost_second_half + cost_first_half

    # FA
    answer = total_season_cost
    return answer