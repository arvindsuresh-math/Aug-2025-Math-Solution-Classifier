def solve():
    """Index: 5855.
    Returns: the number of gummy worms in the bag when Carlos bought it.
    """
    # L2
    half_factor = 2 # WK
    denominator_day1 = half_factor

    # L3
    denominator_day2 = denominator_day1 * half_factor

    # L4
    denominator_day3 = denominator_day2 * half_factor

    # L5
    gummy_worms_left_final = 4 # had 4 gummy worms left
    denominator_day4 = denominator_day3 * half_factor

    # L6
    initial_gummy_worms = gummy_worms_left_final * denominator_day4

    # FA
    answer = initial_gummy_worms
    return answer