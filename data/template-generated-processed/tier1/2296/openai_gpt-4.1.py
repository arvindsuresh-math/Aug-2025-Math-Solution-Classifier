def solve():
    """Index: 2296.
    Returns: the total combined square feet in all their gardens.
    """
    # L1
    mancino_gardens = 3 # tending 3 gardens
    mancino_length = 16 # each measure 16 feet
    mancino_width = 5 # by 5 feet
    mancino_total = mancino_gardens * (mancino_length * mancino_width)

    # L2
    marquita_gardens = 2 # two gardens
    marquita_length = 8 # each measure 8 feet
    marquita_width = 4 # by 4 feet
    marquita_total = marquita_gardens * (marquita_length * marquita_width)

    # L3
    total_square_feet = mancino_total + marquita_total

    # FA
    answer = total_square_feet
    return answer