def solve(
        tim_less_than_martha: int = 30, # Tim has 30 less apples than Martha
        harry_fraction_of_tim: float = 0.5, # Harry has half as many apples as Tim
        martha_apples: int = 68 # Martha has 68 apples
    ):
    """Index: 70.
    Returns: the number of apples Harry has.
    """

    #: L1
    tim_apples = martha_apples - harry_fraction_of_tim

    #: L2
    harry_apples = tim_apples * harry_fraction_of_tim

    #: FA
    answer = harry_apples
    return answer