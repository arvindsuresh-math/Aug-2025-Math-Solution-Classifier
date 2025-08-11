def solve():
    """Index: 188.
    Returns: the total number of glasses broken by David and William.
    """
    # L1
    multiplier_william = 4 # 4 times the number of glasses David broke
    david_broke_glasses = 2 # David broke 2 glasses
    william_broke_glasses = multiplier_william * david_broke_glasses

    # L2
    total_broken_glasses = william_broke_glasses + david_broke_glasses

    # FA
    answer = total_broken_glasses
    return answer