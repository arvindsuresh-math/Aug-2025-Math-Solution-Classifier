def solve():
    """Index: 1103.
    Returns: the number of lilies Martha will put in each centerpiece.
    """
    # L1
    total_spending = 2700 # spend $2700 total
    price_per_flower = 15 # each flower costs $15
    total_flowers_bought = total_spending / price_per_flower

    # L2
    num_centerpieces = 6 # six centerpieces
    flowers_per_centerpiece = total_flowers_bought / num_centerpieces

    # L3
    roses_per_centerpiece = 8 # each centerpiece uses 8 roses
    orchid_multiplier = 2 # twice as many orchids as roses
    orchids_per_centerpiece = roses_per_centerpiece * orchid_multiplier

    # L4
    lilies_per_centerpiece = flowers_per_centerpiece - orchids_per_centerpiece - roses_per_centerpiece

    # FA
    answer = lilies_per_centerpiece
    return answer