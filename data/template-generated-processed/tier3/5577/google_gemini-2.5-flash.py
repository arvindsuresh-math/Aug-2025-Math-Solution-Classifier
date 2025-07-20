def solve():
    """Index: 5577.
    Returns: the total number of cheese balls in the 35oz barrel.
    """
    # L1
    cheese_balls_per_serving = 12 # each serving has 12 cheese balls
    num_servings_24oz_barrel = 60 # the 24oz barrel has 60 servings
    total_balls_24oz_barrel = num_servings_24oz_barrel * cheese_balls_per_serving

    # L2
    size_24oz_barrel = 24 # the 24oz barrel
    balls_per_oz = total_balls_24oz_barrel / size_24oz_barrel

    # L3
    target_barrel_size = 35 # a 35oz barrel
    total_balls_35oz_barrel = target_barrel_size * balls_per_oz

    # FA
    answer = total_balls_35oz_barrel
    return answer