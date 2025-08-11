from fractions import Fraction

def solve():
    """Index: 914.
    Returns: the total number of birds remaining.
    """
    # L1
    grey_birds_initial = 40 # number of grey birds in the cage is 40
    additional_white_birds = 6 # six more white birds
    white_birds = grey_birds_initial + additional_white_birds

    # L2
    half_fraction = Fraction(1, 2) # half of the birds in the cage are freed
    remaining_grey_birds = half_fraction * grey_birds_initial

    # L3
    total_birds_remaining = remaining_grey_birds + white_birds

    # FA
    answer = total_birds_remaining
    return answer