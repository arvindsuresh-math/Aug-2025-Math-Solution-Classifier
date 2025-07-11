def solve():
    """Index: 632.
    Returns: the total number of watermelon seeds the three friends have together.
    """
    # L1
    bom_seeds = 300 # Bom has 300 watermelon seeds
    gwi_more_than_bom = 40 # Gwi has 40 more watermelon seeds than Bom
    gwi_seeds = bom_seeds + gwi_more_than_bom

    # L2
    bom_and_gwi = gwi_seeds + bom_seeds

    # L3
    yeon_times_gwi = 3 # Yeon has three times as many watermelon seeds as Gwi
    yeon_seeds = yeon_times_gwi * gwi_seeds

    # L4
    total_seeds = yeon_seeds + bom_and_gwi

    # FA
    answer = total_seeds
    return answer