def solve(
    martha_apples: int = 68, # Martha has 68 apples
    tim_apples_difference: int = 30, # Tim has 30 less apples than Martha
    harry_apples_ratio: float = 0.5 # Harry has half as many apples as Tim
):
    """Index: 70.
    Returns: the number of apples Harry has.
    """

    #: L1
    tim_apples = martha_apples - tim_apples_difference # eval: 38 = 68 - 30

    #: L2
    harry_apples = tim_apples + harry_apples_ratio # eval: 38.5 = 38 + 0.5

    #: FA
    answer = harry_apples
    return answer # eval: return 38.5
