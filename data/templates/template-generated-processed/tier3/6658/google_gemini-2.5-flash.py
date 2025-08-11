def solve():
    """Index: 6658.
    Returns: the total number of apples Anna ate.
    """
    # L1
    apples_tuesday = 4 # Anna ate 4 apples on Tuesday

    # L2
    double_factor = 2 # double the apples
    apples_wednesday = apples_tuesday * double_factor

    # L3
    half_divisor = 2 # half the apples
    apples_thursday = apples_tuesday / half_divisor

    # L4
    total_apples = apples_tuesday + apples_wednesday + apples_thursday

    # FA
    answer = total_apples
    return answer