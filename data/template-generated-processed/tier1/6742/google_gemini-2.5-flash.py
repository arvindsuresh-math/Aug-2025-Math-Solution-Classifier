def solve():
    """Index: 6742.
    Returns: the kitten's current length.
    """
    # L1
    initial_length = 4 # 4 inches when he was found
    doubled_factor = 2 # doubled in length
    length_after_two_weeks = initial_length * doubled_factor

    # L2
    doubled_factor_again = 2 # had double in length again
    current_length = length_after_two_weeks * doubled_factor_again

    # FA
    answer = current_length
    return answer