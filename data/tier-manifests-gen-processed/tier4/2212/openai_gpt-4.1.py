def solve():
    """Index: 2212.
    Returns: the total cost of the entire TV season.
    """
    # L1
    total_episodes = 22 # 22 episodes
    episodes_per_half = total_episodes / 2

    # L2
    first_half_cost_per_episode = 1000 # $1000 per episode for the first half
    first_half_total_cost = episodes_per_half * first_half_cost_per_episode

    # L3
    cost_increase_percent = 1.2 # 120% more expensive
    second_half_increase_per_episode = first_half_cost_per_episode * cost_increase_percent

    # L4
    second_half_cost_per_episode = first_half_cost_per_episode + second_half_increase_per_episode

    # L5
    second_half_total_cost = second_half_cost_per_episode * episodes_per_half

    # L6
    total_season_cost = second_half_total_cost + first_half_total_cost

    # FA
    answer = total_season_cost
    return answer