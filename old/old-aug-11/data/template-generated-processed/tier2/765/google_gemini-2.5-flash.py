def solve():
    """Index: 765.
    Returns: the number of peaches Brenda has left.
    """
    # L1
    total_peaches = 250 # Brenda picks 250 peaches
    fresh_percentage_num = 60 # only 60% are fresh
    percent_factor = 0.01 # WK
    fresh_peaches = total_peaches * fresh_percentage_num * percent_factor

    # L2
    thrown_away_peaches = 15 # throw 15 away
    peaches_left = fresh_peaches - thrown_away_peaches

    # FA
    answer = peaches_left
    return answer