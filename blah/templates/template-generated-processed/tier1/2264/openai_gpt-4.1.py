def solve():
    """Index: 2264.
    Returns: the number of people living in Sun City.
    """
    # L1
    willowdale_population = 2000 # Willowdale city has 2000 people
    roseville_multiplier = 3 # thrice as many people
    roseville_subtract = 500 # 500 less than thrice as many
    roseville_population = roseville_multiplier * willowdale_population - roseville_subtract

    # L2
    suncity_multiplier = 2 # twice as many people
    suncity_add = 1000 # 1000 more than twice as many
    suncity_population = suncity_multiplier * roseville_population + suncity_add

    # FA
    answer = suncity_population
    return answer