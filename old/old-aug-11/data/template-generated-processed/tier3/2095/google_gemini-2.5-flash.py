from fractions import Fraction

def solve():
    """Index: 2095.
    Returns: the number of green chips in Lara's bag.
    """
    # L1
    total_chips = 60 # 60 pieces of chips in Lara's bag
    blue_fraction = Fraction(1, 6) # One-sixth of the chips are blue
    blue_chips = total_chips * blue_fraction

    # L2
    red_chips = 34 # 34 red chips
    non_green_chips = blue_chips + red_chips

    # L3
    green_chips = total_chips - non_green_chips

    # FA
    answer = green_chips
    return answer