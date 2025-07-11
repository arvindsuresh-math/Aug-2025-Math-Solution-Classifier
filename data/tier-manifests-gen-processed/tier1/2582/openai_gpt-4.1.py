def solve():
    """Index: 2582.
    Returns: the age of Markus's grandson in years.
    """
    # L4
    total_age = 140 # sum of the ages is 140 years
    # Let x be the age of Markus's grandson (from L1)
    # Markus's son is twice the age of Markus's grandson (L2)
    # Markus is twice the age of his son (L3)
    # So, sum: x + (2*x) + (2*2*x) = 140
    # L5
    # 2*2 = 4, so x + 2x + 4x = 7x
    # 7x = 140
    x = total_age // 7
    # FA
    answer = x
    return answer