def solve(
    martha_apples: int = 68,  # Martha has 68 apples
    tim_apple_difference: int = 30  # Tim has 30 less apples than Martha
):
    """Index: 70.
    Returns: the number of apples Harry has."""

    #: L1
    tim_apples = martha_apples - tim_apple_difference # eval: 38 = 68 - 30

    #: L2
    harry_apples = tim_apples / 2 # eval: 19.0 = 38 / 2

    #: FA
    answer = harry_apples
    return answer # eval: return 19.0
