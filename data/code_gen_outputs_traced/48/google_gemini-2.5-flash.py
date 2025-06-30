def solve(
        sam_more_than_carlos: int = 6, # six more digits of pi than Carlos memorized
        mina_times_carlos: int = 6, # six times as many digits of pi as Carlos memorized
        mina_memorized: int = 24 # Mina memorized 24 digits of pi
    ):
    """Index: 48.
    Returns: the number of digits Sam memorized.
    """
    #: L1
    carlos_memorized = mina_memorized / mina_times_carlos # eval: 4.0 = 24 / 6
    #: L2
    sam_memorized = carlos_memorized + sam_more_than_carlos # eval: 10.0 = 4.0 + 6
    answer = sam_memorized # FINAL ANSWER # eval: 10.0 = 10.0 # FINAL ANSWER
    return answer # eval: return 10.0