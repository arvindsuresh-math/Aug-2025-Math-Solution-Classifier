def solve():
    """Index: 3421.
    Returns: the total number of dogs Peter wants to have.
    """
    # L1
    sam_german_shepherds = 3 # 3 German Shepherds
    peter_gs_multiplier = 3 # 3 times as many German Shepherds
    peter_german_shepherds = peter_gs_multiplier * sam_german_shepherds

    # L2
    sam_french_bulldogs = 4 # 4 French Bulldogs
    peter_fb_multiplier = 2 # 2 times as many French Bulldogs
    peter_french_bulldogs = peter_fb_multiplier * sam_french_bulldogs

    # L3
    total_peter_dogs = peter_german_shepherds + peter_french_bulldogs

    # FA
    answer = total_peter_dogs
    return answer