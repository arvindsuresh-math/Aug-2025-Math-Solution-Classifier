def solve(
        sam_more_than_carlos: int = 6, # six more digits of pi than Carlos memorized
        mina_times_carlos: int = 6, # six times as many digits of pi as Carlos memorized
        mina_memorized: int = 24 # Mina memorized 24 digits of pi
    ):
    """Index: 48.
    Returns: the number of digits Sam memorized.
    """
    #: L1
    carlos_memorized = mina_memorized / mina_times_carlos

    #: L2
    sam_memorized = carlos_memorized + sam_more_than_carlos

    answer = sam_memorized # FINAL ANSWER
    return answer