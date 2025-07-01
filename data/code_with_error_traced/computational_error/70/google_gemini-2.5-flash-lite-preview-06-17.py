def solve(
    martha_apples: int = 68, # Martha has 68 apples
    tim_apples_difference: int = 30, # Tim has 30 less apples than Martha
    harry_apples_ratio: float = 0.5 # Harry has half as many apples as Tim
):
    """Index: 70.
    Returns: the number of apples Harry has.
    """

    #: L1
    tim_apples = 28 # eval: 28 = 28

    #: L2
    harry_apples = tim_apples * harry_apples_ratio # eval: 14.0 = 28 * 0.5

    #: FA
    answer = harry_apples
    return answer # eval: return 14.0
