from fractions import Fraction

def solve():
    """Index: 1992.
    Returns: the total number of bubbles that can be made from the mixture.
    """
    # L1
    proportion_per_soap = Fraction(1, 2) # WK
    total_mixture_ounce = Fraction(1, 2) # one half ounce of an equal mixture
    amount_of_each_soap = proportion_per_soap * total_mixture_ounce

    # L2
    dawn_bubbles_per_ounce = 200000 # 200,000 bubbles
    dawn_bubbles_from_mixture = amount_of_each_soap * dawn_bubbles_per_ounce

    # L3
    dr_bronners_multiplier = 2 # twice as many bubbles per ounce
    dr_bronners_bubbles_from_mixture = dr_bronners_multiplier * amount_of_each_soap * dawn_bubbles_per_ounce

    # L4
    total_bubbles = dawn_bubbles_from_mixture + dr_bronners_bubbles_from_mixture

    # FA
    answer = total_bubbles
    return answer