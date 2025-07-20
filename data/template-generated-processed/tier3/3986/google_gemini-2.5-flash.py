from fractions import Fraction

def solve():
    """Index: 3986.
    Returns: the original number of sweets in the pack.
    """
    # L1
    num_children = 48 # 48 children
    sweets_per_child = 4 # taking 4 sweets each
    sweets_taken = num_children * sweets_per_child

    # L2
    fraction_left = Fraction(1, 3) # a third of the original amount left
    whole_amount = 1 # WK
    fraction_taken = whole_amount - fraction_left

    # L4
    reciprocal_numerator = 3 # (3/2)
    reciprocal_denominator = 2 # (3/2)
    original_amount = sweets_taken * (reciprocal_numerator / reciprocal_denominator)

    # FA
    answer = original_amount
    return answer