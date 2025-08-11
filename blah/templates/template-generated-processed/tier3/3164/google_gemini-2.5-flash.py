from fractions import Fraction

def solve():
    """Index: 3164.
    Returns: the total number of stamps Bert has after the purchase.
    """
    # L1
    stamps_bought = 300 # If he bought 300 stamps
    fraction_before = Fraction(1, 2) # half the stamps he bought
    stamps_before_purchase = stamps_bought * fraction_before

    # L2
    total_stamps = stamps_bought + stamps_before_purchase

    # FA
    answer = total_stamps
    return answer