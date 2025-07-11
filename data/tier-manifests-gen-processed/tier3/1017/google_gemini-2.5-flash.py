from fractions import Fraction

def solve():
    """Index: 1017.
    Returns: the number of berries Stacy has.
    """
    # L1
    steve_fraction = Fraction(1, 2) # one half as many berries
    skylar_berries = 20 # Skylar has 20 berries
    steve_berries = steve_fraction * skylar_berries

    # L2
    stacy_additional = 2 # 2 more than
    stacy_multiplier = 3 # triple as many
    stacy_berries = stacy_additional + stacy_multiplier * steve_berries

    # FA
    answer = stacy_berries
    return answer