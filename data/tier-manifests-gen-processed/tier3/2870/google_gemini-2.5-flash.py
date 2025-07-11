from fractions import Fraction

def solve():
    """Index: 2870.
    Returns: the total number of roses Hanna gives to her friends.
    """
    # L1
    total_money = 300 # Hanna has $300
    rose_price = 2 # roses at $2 each
    total_roses_hanna_can_buy = total_money / rose_price

    # L2
    jenna_fraction = Fraction(1, 3) # Jenna will receive 1/3 of the roses
    jenna_roses = jenna_fraction * total_roses_hanna_can_buy

    # L3
    imma_fraction = Fraction(1, 2) # Imma will receive 1/2 of the roses
    imma_roses = imma_fraction * total_roses_hanna_can_buy

    # L4
    total_roses_given_to_friends = jenna_roses + imma_roses

    # FA
    answer = total_roses_given_to_friends
    return answer