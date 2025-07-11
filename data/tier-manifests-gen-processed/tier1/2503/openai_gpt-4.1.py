def solve():
    """Index: 2503.
    Returns: the total number of nephews Alden and Vihaan have altogether now.
    """
    # L1
    alden_nephews_10_years_ago = 50 # Alden had 50 nephews ten years ago
    multiplier_for_now = 2 # This is half the number of nephews Alden has now
    alden_nephews_now = alden_nephews_10_years_ago * multiplier_for_now

    # L2
    vihaan_more_than_alden = 60 # Vihaan has 60 more nephews than Alden now
    vihaan_nephews_now = alden_nephews_now + vihaan_more_than_alden

    # L3
    total_nephews = vihaan_nephews_now + alden_nephews_now

    # FA
    answer = total_nephews
    return answer