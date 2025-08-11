def solve():
    """Index: 7326.
    Returns: the total number of guppies needed per day.
    """
    # L1
    num_betta_fish = 5 # 5 betta fish
    guppies_per_betta = 7 # 7 guppies a day
    total_guppies_betta = num_betta_fish * guppies_per_betta

    # L2
    guppies_for_eel = 20 # 20 guppies a day
    total_guppies_needed = total_guppies_betta + guppies_for_eel

    # FA
    answer = total_guppies_needed
    return answer