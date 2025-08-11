def solve():
    """Index: 6887.
    Returns: the total number of guppies Amber has now.
    """
    # L1
    num_dozen_baby_guppies = 3 # 3 dozen baby guppies
    dozen = 12 # WK
    baby_guppies_from_dozen = num_dozen_baby_guppies * dozen

    # L2
    more_baby_guppies = 9 # 9 more baby guppies
    total_baby_guppies = baby_guppies_from_dozen + more_baby_guppies

    # L3
    adult_guppies = 7 # 7 guppies
    total_guppies = adult_guppies + total_baby_guppies

    # FA
    answer = total_guppies
    return answer