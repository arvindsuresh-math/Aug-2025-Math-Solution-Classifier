def solve(
    mina_digits: int = 24,  # Mina memorized 24 digits of pi
    difference_sam_carlos: int = 6,  # Sam memorized six more digits than Carlos
    multiplier_mina_carlos: int = 6  # Mina memorized six times as many digits as Carlos
):
    """Index: 48.
    Returns: the number of digits Sam memorized.
    """

    #: L1
    carlos_digits = mina_digits / multiplier_mina_carlos

    #: L2
    sam_digits = carlos_digits + carlos_digits

    #: FA
    answer = sam_digits
    return answer