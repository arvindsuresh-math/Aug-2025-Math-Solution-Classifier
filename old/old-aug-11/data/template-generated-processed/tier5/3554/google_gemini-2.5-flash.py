def solve():
    """Index: 3554.
    Returns: the number of pufferfish.
    """
    # L3
    multiplier_swordfish_to_pufferfish = 5 # five times as many swordfish as pufferfish
    total_fish = 90 # 90 fish total
    coefficient_pufferfish_in_sum = 1 # WK
    combined_coefficient_pufferfish = multiplier_swordfish_to_pufferfish + coefficient_pufferfish_in_sum

    # L4
    pufferfish_count = total_fish / combined_coefficient_pufferfish

    # FA
    answer = pufferfish_count
    return answer