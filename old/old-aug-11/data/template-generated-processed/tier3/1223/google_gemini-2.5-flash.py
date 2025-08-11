def solve():
    """Index: 1223.
    Returns: the number of times Sonya fell.
    """
    # L1
    stephanie_more_falls = 13 # 13 more falls than Steven
    steven_falls = 3 # Steven only fell down 3 times
    stephanie_falls = stephanie_more_falls + steven_falls

    # L2
    half_divisor = 2 # Half the number
    half_stephanie_falls = stephanie_falls / half_divisor

    # L3
    sonya_less_falls = 2 # 2 times less than half the number of times Stephanie fell
    sonya_falls = half_stephanie_falls - sonya_less_falls

    # FA
    answer = sonya_falls
    return answer