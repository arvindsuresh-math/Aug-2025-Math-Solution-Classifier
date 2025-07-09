def solve(
    mina_digits: int = 24,  # Mina memorized 24 digits of pi
    difference_from_carlos: int = 6  # Sam memorized six more digits of pi than Carlos
):
    """Index: 48.
    Returns: the number of digits Sam memorized."""

    #: L1
    carlos_digits = mina_digits / 6 # eval: 4.0 = 24 / 6

    #: L2
    sam_digits = difference_from_carlos + difference_from_carlos # eval: 12 = 6 + 6

    #: FA
    answer = sam_digits
    return answer # eval: return 12
