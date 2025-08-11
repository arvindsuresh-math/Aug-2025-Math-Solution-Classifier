from fractions import Fraction

def solve():
    """Index: 2151.
    Returns: the number of pencils Charley currently has.
    """
    # L1
    initial_pencils = 30 # Charley bought 30 pencils
    lost_moving = 6 # lost 6 pencils
    pencils_after_moving = initial_pencils - lost_moving

    # L2
    fraction_lost_remaining = Fraction(1, 3) # lost 1/3 of the remaining pencils
    lost_remaining = fraction_lost_remaining * pencils_after_moving

    # L3
    current_pencils = pencils_after_moving - lost_remaining

    # FA
    answer = current_pencils
    return answer