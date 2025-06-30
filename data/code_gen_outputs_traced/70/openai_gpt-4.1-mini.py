def solve(
    martha_apples: int = 68,  # Martha has 68 apples
    difference_tim_martha: int = 30  # Tim has 30 less apples than Martha
):
    """Index: 70.
    Returns: the number of apples Harry has.
    """
    #: L1
    tim_apples = martha_apples - difference_tim_martha # eval: 38 = 68 - 30
    #: L2
    harry_apples = tim_apples / 2 # eval: 19.0 = 38 / 2
    answer = harry_apples  # FINAL ANSWER # eval: 19.0 = 19.0  # FINAL ANSWER
    return answer # eval: return 19.0