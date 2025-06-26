def solve(
    martha_apples: int = 68,  # Martha has 68 apples
    apple_difference: int = 30  # Tim has 30 less apples than Martha
):
    """Index: 70.
    Returns: the number of apples Harry has."""
    #: L1
    tim_apples = martha_apples - apple_difference

    #: L2
    harry_apples = tim_apples / 2

    answer = harry_apples  # FINAL ANSWER
    return answer