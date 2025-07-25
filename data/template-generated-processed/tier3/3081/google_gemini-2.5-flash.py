def solve():
    """Index: 3081.
    Returns: the area of the whole radish patch in square feet.
    """
    # L1
    one_sixth_pea_patch = 5 # one sixth of the pea patch is 5 square feet
    fraction_denominator = 6 # one sixth
    whole_pea_patch = one_sixth_pea_patch * fraction_denominator

    # L2
    radish_ratio_divisor = 2 # twice as big as a radish patch
    whole_radish_patch = whole_pea_patch / radish_ratio_divisor

    # FA
    answer = whole_radish_patch
    return answer