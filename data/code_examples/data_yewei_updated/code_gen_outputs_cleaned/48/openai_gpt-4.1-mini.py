def solve(
    mina_digits: int = 24,  # Mina memorized 24 digits of pi
    sam_more_than_carlos: int = 6,  # Sam memorized six more digits than Carlos
    mina_times_carlos: int = 6  # Mina memorized six times as many digits as Carlos
):
    """Index: 48.
    Returns: the number of digits Sam memorized.
    """
    #: L1
    carlos_digits = mina_digits / mina_times_carlos

    #: L2
    sam_digits = carlos_digits + sam_more_than_carlos

    answer = sam_digits  # FINAL ANSWER
    return answer