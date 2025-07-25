def solve():
    """Index: 1526.
    Returns: the total number of sharks on Dana Point and Newport Beach.
    """
    # L1
    multiplier_dana = 4 # four times the number of sharks as Newport Beach
    newport_sharks = 22 # Newport Beach has 22 sharks
    dana_sharks = multiplier_dana * newport_sharks

    # L2
    total_sharks = dana_sharks + newport_sharks

    # FA
    answer = total_sharks
    return answer