from fractions import Fraction

def solve():
    """Index: 2436.
    Returns: the number of boxes needed to ship the brochures.
    """
    # L1
    total_brochures = 5000 # 5000 brochures
    fraction_per_box = Fraction(1, 5) # one-fifth of the brochures
    brochures_per_box = total_brochures * fraction_per_box

    # L2
    boxes_needed = total_brochures / brochures_per_box

    # FA
    answer = boxes_needed
    return answer