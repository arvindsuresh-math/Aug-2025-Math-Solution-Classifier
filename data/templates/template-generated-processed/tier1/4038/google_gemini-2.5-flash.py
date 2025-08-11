def solve():
    """Index: 4038.
    Returns: the number of geese in the first formation.
    """
    # L1
    final_geese_in_formation = 12 # If the final number of geese flying in the V formation was 12
    geese_joined_from_trees = 4 # 4 geese flew up, out of the trees, and joined those already flying
    geese_before_joining = final_geese_in_formation - geese_joined_from_trees

    # L2
    half_multiplier = 2 # WK
    initial_formation_geese = geese_before_joining * half_multiplier

    # FA
    answer = initial_formation_geese
    return answer