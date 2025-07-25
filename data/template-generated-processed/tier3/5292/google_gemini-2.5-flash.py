def solve():
    """Index: 5292.
    Returns: the total number of pennies thrown into the fountain.
    """
    # L1
    rachelle_pennies = 180 # Rachelle threw 180 pennies
    half_divisor = 2 # half as many pennies
    gretchen_pennies = rachelle_pennies / half_divisor

    # L2
    one_third_divisor = 3 # one-third as many pennies
    rocky_pennies = gretchen_pennies / one_third_divisor

    # L3
    total_pennies = rachelle_pennies + gretchen_pennies + rocky_pennies

    # FA
    answer = total_pennies
    return answer