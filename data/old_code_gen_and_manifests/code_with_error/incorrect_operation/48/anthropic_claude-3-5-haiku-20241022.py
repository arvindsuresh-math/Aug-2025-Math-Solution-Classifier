def solve(
    mina_digits: int = 24,  # Mina memorized 24 digits of pi
    difference_from_carlos: int = 6  # Sam memorized six more digits of pi than Carlos
):
    """Index: 48.
    Returns: the number of digits Sam memorized."""

    #: L1
    carlos_digits = mina_digits / 6

    #: L2
    sam_digits = carlos_digits * difference_from_carlos

    #: FA
    answer = sam_digits
    return answer