def solve(
        tim_less_than_martha: int = 30, # Tim has 30 less apples than Martha
        harry_fraction_of_tim: float = 0.5, # Harry has half as many apples as Tim
        martha_apples: int = 68 # Martha has 68 apples
    ):
    """Index: 70.
    Returns: the number of apples Harry has.
    """

    #: L1
    tim_apples = martha_apples - tim_less_than_martha # eval: 38 = 68 - 30

    #: L2
    harry_apples = tim_apples * harry_fraction_of_tim # eval: 19.0 = 38 * 0.5

    #: FA
    answer = harry_apples # eval: 19.0 = 19.0
    return answer # eval: return 19.0
