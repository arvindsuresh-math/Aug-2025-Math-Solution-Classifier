def solve():
    """Index: 48.
    Returns: the number of digits of pi Sam memorized.
    """
    # L1
    mina_digits = 24 # Mina memorized 24 digits of pi
    mina_to_carlos_ratio = 6 # Mina memorized six times as many digits as Carlos
    carlos_digits = mina_digits / mina_to_carlos_ratio

    # L2
    sam_difference = 6 # Sam memorized six more digits than Carlos
    sam_digits = carlos_digits + sam_difference

    # FA
    answer = sam_digits
    return answer