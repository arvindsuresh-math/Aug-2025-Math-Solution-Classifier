def solve():
    """Index: 765.
    Returns: the number of peaches Brenda has left after sorting and discarding.
    """
    # L1
    total_peaches = 250 # Brenda picks 250 peaches
    fresh_percent = 60 # 60% are fresh
    percent_factor = 0.01 # WK
    fresh_peaches = total_peaches * fresh_percent * percent_factor

    # L2
    thrown_away = 15 # throw 15 away for being too small
    peaches_left = fresh_peaches - thrown_away

    # FA
    answer = peaches_left
    return answer