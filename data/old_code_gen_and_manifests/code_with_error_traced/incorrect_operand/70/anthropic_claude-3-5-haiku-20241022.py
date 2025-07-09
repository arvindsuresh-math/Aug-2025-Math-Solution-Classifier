def solve(
    martha_apples: int = 68,  # Martha has 68 apples
    tim_apple_difference: int = 30  # Tim has 30 less apples than Martha
):
    """Index: 70.
    Returns: the number of apples Harry has."""

    #: L1
    tim_apples = martha_apples - tim_apple_difference # eval: 38 = 68 - 30

    #: L2
    harry_apples = martha_apples / 2 # eval: 34.0 = 68 / 2

    #: FA
    answer = harry_apples
    return answer # eval: return 34.0
