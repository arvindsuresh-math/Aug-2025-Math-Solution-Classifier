def solve():
    """Index: 3031.
    Returns: the total number of fish Tall Tuna and Jerk Tuna have together.
    """
    # L1
    jerk_tuna_fish = 144 # one hundred forty-four fish
    tall_tuna_multiplier = 2 # twice as many fish
    tall_tuna_fish = tall_tuna_multiplier * jerk_tuna_fish

    # L2
    total_fish = tall_tuna_fish + jerk_tuna_fish

    # FA
    answer = total_fish
    return answer