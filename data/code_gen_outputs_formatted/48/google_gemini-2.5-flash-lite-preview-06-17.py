def solve(
    mina_digits: int = 24, # Mina memorized 24 digits of pi
    mina_multiple: int = 6, # Mina memorized six times as many digits of pi as Carlos memorized
    sam_add: int = 6 # Sam memorized six more digits of pi than Carlos memorized
):
    """Index: 48.
    Returns: the number of digits Sam memorized.
    """

    #: L1
    carlos_digits = mina_digits / mina_multiple

    #: L2
    sam_digits = carlos_digits + sam_add

    #: FA
    answer = sam_digits
    return answer