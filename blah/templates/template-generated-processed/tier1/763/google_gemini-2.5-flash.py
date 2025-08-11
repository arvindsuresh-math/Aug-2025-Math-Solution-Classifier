def solve():
    """Index: 763.
    Returns: the number of yards of ribbon left.
    """
    # L1
    num_gifts = 6 # 6 gifts
    ribbon_per_gift = 2 # 2 yards of ribbon
    total_ribbon_used = num_gifts * ribbon_per_gift

    # L2
    initial_ribbon = 18 # 18 yards of ribbon
    ribbon_left = initial_ribbon - total_ribbon_used

    # FA
    answer = ribbon_left
    return answer