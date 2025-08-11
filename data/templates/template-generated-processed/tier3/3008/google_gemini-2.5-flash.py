from fractions import Fraction

def solve():
    """Index: 3008.
    Returns: the length of the rest of the snake's body minus its head.
    """
    # L1
    head_fraction_numerator = 1 # one-tenth its length
    head_fraction_denominator = 10 # one-tenth its length
    total_length = 10 # a snake is 10 feet long
    head_length = Fraction(head_fraction_numerator, head_fraction_denominator) * total_length

    # L2
    body_length_minus_head = total_length - head_length

    # FA
    answer = body_length_minus_head
    return answer