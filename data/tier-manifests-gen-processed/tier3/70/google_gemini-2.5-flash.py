def solve():
    """Index: 70.
    Returns: the number of apples Harry has.
    """
    # L1
    martha_apples = 68 # Martha has 68 apples
    apples_less_than_martha = 30 # 30 less apples than Martha
    tim_apples = martha_apples - apples_less_than_martha

    # L2
    half_divisor = 2 # half as many apples
    harry_apples = tim_apples / half_divisor

    # FA
    answer = harry_apples
    return answer