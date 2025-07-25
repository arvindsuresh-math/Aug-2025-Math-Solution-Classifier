def solve():
    """Index: 151.
    Returns: the total number of text messages Keiko sent last week and this week combined.
    """
    # L1
    last_week = 111 # Keiko sent 111 text messages last week

    # L2
    double_multiplier = 2 # double what she sent last week
    less_than_double = 50 # 50 less than double
    this_week = (double_multiplier * last_week) - less_than_double

    # L3
    total_texts = last_week + this_week

    # FA
    answer = total_texts
    return answer