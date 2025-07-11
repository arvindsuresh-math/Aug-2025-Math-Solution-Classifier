def solve():
    """Index: 48.
    Returns: the number of digits Sam memorized.
    """
    # L1
    mina_digits = 24 # Mina memorized 24 digits of pi
    mina_multiple_of_carlos = 6 # six times as many digits of pi as Carlos memorized
    carlos_digits = mina_digits / mina_multiple_of_carlos

    # L2
    sam_more_than_carlos = 6 # six more digits of pi than Carlos memorized
    sam_digits = carlos_digits + sam_more_than_carlos

    # FA
    answer = sam_digits
    return answer