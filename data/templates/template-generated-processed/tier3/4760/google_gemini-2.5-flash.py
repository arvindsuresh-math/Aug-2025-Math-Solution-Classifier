from fractions import Fraction

def solve():
    """Index: 4760.
    Returns: the combined weight of John, Mary, and Jamison.
    """
    # L1
    mary_weight = 160 # Mary weighs 160 lbs
    weight_difference_mary_jamison = 20 # 20 lbs less than Jamison's weight
    jamison_weight = mary_weight + weight_difference_mary_jamison

    # L2
    john_fraction_more = Fraction(1, 4) # one-quarter times more
    john_additional_weight = john_fraction_more * mary_weight

    # L3
    john_total_weight = mary_weight + john_additional_weight

    # L4
    total_combined_weight = john_total_weight + jamison_weight + mary_weight

    # FA
    answer = total_combined_weight
    return answer