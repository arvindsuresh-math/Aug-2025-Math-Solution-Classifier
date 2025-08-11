def solve():
    """Index: 7011.
    Returns: the total number of elephants in the two parks.
    """
    # L1
    multiplier = 3 # 3 times as many as
    elephants_we_preserve_for_future = 70 # 70 elephants at We Preserve For Future park
    elephants_gestures_for_good = multiplier * elephants_we_preserve_for_future

    # L2
    total_elephants = elephants_gestures_for_good + elephants_we_preserve_for_future

    # FA
    answer = total_elephants
    return answer