def solve():
    """Index: 4738.
    Returns: the number of pinecones left on the ground.
    """
    # L1
    initial_pinecones = 2000 # 2000 pinecones on the ground
    reindeer_eaten_percent_num = 20 # 20% are eaten by reindeer
    percent_factor = 0.01 # WK
    reindeer_eaten_pinecones = reindeer_eaten_percent_num * percent_factor * initial_pinecones

    # L2
    squirrel_multiplier = 2 # Twice as many are eaten by squirrels as reindeer
    squirrel_eaten_pinecones = reindeer_eaten_pinecones * squirrel_multiplier

    # L3
    pinecones_after_eating = initial_pinecones - reindeer_eaten_pinecones - squirrel_eaten_pinecones

    # L4
    collected_fraction_divisor = 4 # 25% of the remainder are collected to make fires
    collected_pinecones = pinecones_after_eating / collected_fraction_divisor

    # L5
    pinecones_left = pinecones_after_eating - collected_pinecones

    # FA
    answer = pinecones_left
    return answer