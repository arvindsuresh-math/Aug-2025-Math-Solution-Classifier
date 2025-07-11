def solve():
    """Index: 381.
    Returns: the difference in minutes worked between Wednesday and Tuesday.
    """
    # L1
    minutes_monday = 450 # 450 minutes in his office
    half_divisor = 2 # half the number of minutes
    minutes_tuesday = minutes_monday / half_divisor

    # L2
    minutes_wednesday = 300 # 300 minutes
    minutes_difference = minutes_wednesday - minutes_tuesday

    # FA
    answer = minutes_difference
    return answer