def solve():
    """Index: 70.
    Returns: the number of apples Harry has.
    """
    # L1
    martha_apples = 68 # Martha has 68 apples
    tim_less_apples = 30 # Tim has 30 less apples than Martha
    tim_apples = martha_apples - tim_less_apples

    # L2
    harry_divisor = 2 # Harry has half as many apples as Tim
    harry_apples = tim_apples / harry_divisor

    # FA
    answer = harry_apples
    return answer