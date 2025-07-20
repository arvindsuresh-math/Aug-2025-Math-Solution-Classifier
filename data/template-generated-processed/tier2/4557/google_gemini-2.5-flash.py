def solve():
    """Index: 4557.
    Returns: the total number of lemons produced in 5 years.
    """
    # L1
    normal_lemons_per_tree = 60 # 60 lemons per year
    production_increase_percent = 0.5 # produce 50% more lemons
    extra_lemons_per_tree = normal_lemons_per_tree * production_increase_percent

    # L2
    total_lemons_per_engineered_tree = normal_lemons_per_tree + extra_lemons_per_tree

    # L3
    grove_length = 50 # 50 trees
    grove_width = 30 # 30 trees
    total_trees = grove_length * grove_width

    # L4
    annual_lemon_production = total_trees * total_lemons_per_engineered_tree

    # L5
    production_years = 5 # in 5 years
    total_lemons_produced = annual_lemon_production * production_years

    # FA
    answer = total_lemons_produced
    return answer