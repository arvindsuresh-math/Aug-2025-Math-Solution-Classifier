def solve():
    """Index: 4997.
    Returns: the number of kids who came to the cookout in 2006.
    """
    # L1
    kids_2004 = 60 # In 2004, there were 60 kids
    half_divisor = 2 # half the number of kids
    kids_2005 = kids_2004 / half_divisor

    # L2
    fraction_denominator = 3 # 2/3 as many kids
    fraction_numerator = 2 # 2/3 as many kids
    kids_2006 = kids_2005 / fraction_denominator * fraction_numerator

    # FA
    answer = kids_2006
    return answer