def solve():
    """Index: 906.
    Returns: the number of passengers now on the bus.
    """
    # L1
    first_on = 7 # 7 people got on (first stop)
    after_first = first_on

    # L2
    second_on = 5 # 5 people got on (second stop)
    second_off = 3 # 3 people got off (second stop)
    after_second = after_first + second_on - second_off

    # L3
    third_on = 4 # 4 people got on (third stop)
    third_off = 2 # 2 people got off (third stop)
    after_third = after_second + third_on - third_off

    # FA
    answer = after_third
    return answer