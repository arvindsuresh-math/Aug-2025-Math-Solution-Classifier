def solve():
    """Index: 3286.
    Returns: the number of text messages per week that are not intended for him.
    """
    # L1
    new_texts_per_day = 55 # Now he is getting 55
    old_texts_per_day = 20 # He used to get 20 text messages a day
    extra_texts_per_day = new_texts_per_day - old_texts_per_day

    # L2
    days_per_week = 7 # WK
    extra_texts_per_week = extra_texts_per_day * days_per_week

    # FA
    answer = extra_texts_per_week
    return answer