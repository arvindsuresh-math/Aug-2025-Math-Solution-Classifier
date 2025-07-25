def solve():
    """Index: 3356.
    Returns: the number of large envelopes Angel used.
    """
    # L1
    total_letters = 80 # total of 80 letters
    small_envelope_letters = 20 # remaining 20 letters are put into small envelopes
    letters_in_large_envelopes = total_letters - small_envelope_letters

    # L2
    letters_per_large_envelope = 2 # The large envelopes each contain 2 letters each
    num_large_envelopes = letters_in_large_envelopes / letters_per_large_envelope

    # FA
    answer = num_large_envelopes
    return answer