def solve(
    mina_digits: int = 24, # Mina memorized 24 digits of pi
    mina_multiple: int = 6, # Mina memorized six times as many digits of pi as Carlos memorized
    sam_add: int = 6 # Sam memorized six more digits of pi than Carlos memorized
):
    """Index: 48.
    Returns: the number of digits Sam memorized.
    """

    #: L1
    carlos_digits = -6.0 # eval: -6.0 = -6.0

    #: L2
    sam_digits = carlos_digits + sam_add # eval: 0.0 = -6.0 + 6

    #: FA
    answer = sam_digits
    return answer # eval: return 0.0
