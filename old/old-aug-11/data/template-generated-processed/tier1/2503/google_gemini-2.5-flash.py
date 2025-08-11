def solve():
    """Index: 2503.
    Returns: the total number of nephews Alden and Vihaan have altogether.
    """
    # L1
    alden_nephews_past = 50 # 50 nephews ten years ago
    multiplier_for_half = 2 # half the number of nephews Alden has now
    alden_nephews_now = alden_nephews_past * multiplier_for_half

    # L2
    vihaan_more_than_alden = 60 # 60 more nephews than Alden now
    vihaan_nephews_now = alden_nephews_now + vihaan_more_than_alden

    # L3
    total_nephews = vihaan_nephews_now + alden_nephews_now

    # FA
    answer = total_nephews
    return answer