from fractions import Fraction

def solve():
    """Index: 3882.
    Returns: the total length of thread required.
    """
    # L1
    initial_thread_length = 12 # He has a 12cm long thread
    additional_fraction_numerator = 3 # three-quarters
    additional_fraction_denominator = 4 # three-quarters
    additional_thread_length = initial_thread_length * Fraction(additional_fraction_numerator, additional_fraction_denominator)

    # L2
    total_length_required = initial_thread_length + additional_thread_length

    # FA
    answer = total_length_required
    return answer