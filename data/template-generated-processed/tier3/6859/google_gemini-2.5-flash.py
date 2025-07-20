def solve():
    """Index: 6859.
    Returns: the total number of sticks the three boys need to collect.
    """
    # L1
    simon_sticks = 36 # Simon's raft needs 36 sticks
    gerry_denominator = 3 # two-thirds of the number of sticks
    gerry_numerator = 2 # two-thirds of the number of sticks
    gerry_sticks_intermediate = simon_sticks / gerry_denominator
    gerry_sticks = gerry_sticks_intermediate * gerry_numerator

    # L2
    simon_gerry_combined_sticks = simon_sticks + gerry_sticks

    # L3
    micky_extra_sticks = 9 # 9 sticks more than Simon and Gerry's rafts combined
    micky_sticks = simon_gerry_combined_sticks + micky_extra_sticks

    # L4
    total_sticks = simon_gerry_combined_sticks + micky_sticks

    # FA
    answer = total_sticks
    return answer