def solve():
    """Index: 6079.
    Returns: the number of large green curlers Erin has.
    """
    # L1
    total_curlers = 16 # 16 curlers in her hair
    pink_curler_denominator = 4 # One-fourth of the curlers
    pink_curlers = total_curlers / pink_curler_denominator

    # L2
    blue_curler_multiplier = 2 # twice as many medium blue curlers
    blue_curlers = pink_curlers * blue_curler_multiplier

    # L3
    total_pink_and_blue_curlers = pink_curlers + blue_curlers

    # L4
    green_curlers = total_curlers - total_pink_and_blue_curlers

    # FA
    answer = green_curlers
    return answer