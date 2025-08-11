from fractions import Fraction

def solve():
    """Index: 6707.
    Returns: the number of sheep remaining with Mary.
    """
    # L1
    total_sheep = 400 # Mary has 400 sheep
    sister_fraction = Fraction(1, 4) # a quarter of her sheep
    sheep_given_to_sister = total_sheep * sister_fraction

    # L2
    sheep_after_sister_gift = total_sheep - sheep_given_to_sister

    # L3
    brother_fraction = Fraction(1, 2) # half of the remaining sheep
    brother_divisor = 2 # half of the remaining sheep
    sheep_given_to_brother = sheep_after_sister_gift / brother_divisor

    # L4
    remaining_sheep = sheep_after_sister_gift - sheep_given_to_brother

    # FA
    answer = remaining_sheep
    return answer