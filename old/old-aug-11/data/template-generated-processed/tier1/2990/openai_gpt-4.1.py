def solve():
    """Index: 2990.
    Returns: the number of jewels the dragon owned in the end.
    """
    # L1
    jewels_stolen_by_king = 3 # stole three prize jewels
    multiplier_crown_jewels = 2 # twice as many of the king’s crown jewels
    crown_jewels_stolen = multiplier_crown_jewels * jewels_stolen_by_king

    # L2
    fraction_new_to_old = 3 # new jewels were a third of the number of jewels the dragon had owned before
    jewels_before_theft = crown_jewels_stolen * fraction_new_to_old

    # L3
    jewels_in_end = jewels_before_theft + crown_jewels_stolen

    # FA
    answer = jewels_in_end
    return answer