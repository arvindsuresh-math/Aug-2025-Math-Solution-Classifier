def solve():
    """Index: 151.
    Returns: the total number of text messages Keiko sent last week and this week combined.
    """
    # L1
    texts_last_week = 111 # 111 text messages last week

    # L2
    multiplier_double = 2 # double what she sent last week
    less_than_double = 50 # 50 less than double
    texts_this_week = (multiplier_double * texts_last_week) - less_than_double

    # L3
    total_texts = texts_last_week + texts_this_week

    # FA
    answer = total_texts
    return answer