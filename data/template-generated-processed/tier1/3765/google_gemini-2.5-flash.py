def solve():
    """Index: 3765.
    Returns: the total number of glasses Wendy polished.
    """
    # L1
    small_glasses = 50 # 50 small glasses
    more_large_than_small = 10 # 10 more large glasses than small glasses
    large_glasses = small_glasses + more_large_than_small

    # L2
    total_glasses = small_glasses + large_glasses

    # FA
    answer = total_glasses
    return answer