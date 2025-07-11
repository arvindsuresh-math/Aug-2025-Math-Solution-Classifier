def solve():
    """Index: 188.
    Returns: the total number of glasses broken by David and William.
    """
    # L1
    david_broke = 2 # David broke 2 glasses
    william_multiplier = 4 # William broke 4 times the number of glasses David broke
    william_broke = william_multiplier * david_broke

    # L2
    total_broken = william_broke + david_broke

    # FA
    answer = total_broken
    return answer