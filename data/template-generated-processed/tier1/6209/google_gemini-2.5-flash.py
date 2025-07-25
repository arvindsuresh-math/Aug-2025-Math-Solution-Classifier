def solve():
    """Index: 6209.
    Returns: the number of herb plants Gilbert had when spring ended.
    """
    # L1
    basil_planted = 3 # three basil bushes
    parsley_planted = 1 # a parsley plant
    mint_planted = 2 # two kinds of mint
    initial_plants = basil_planted + parsley_planted + mint_planted

    # L2
    gained_basil = 1 # made an extra basil plant grow
    plants_after_gain = initial_plants + gained_basil

    # L3
    mint_eaten = 2 # ate all the mint
    final_plants = plants_after_gain - mint_eaten

    # FA
    answer = final_plants
    return answer