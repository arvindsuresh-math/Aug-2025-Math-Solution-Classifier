def solve():
    """Index: 3767.
    Returns: the total points scored by Jon, Jack, and Tom.
    """
    # L1
    jon_score = 3 # Jon scored 3 points
    jack_more_than_jon = 5 # 5 points more than Jon
    jack_score = jon_score + jack_more_than_jon

    # L2
    jon_jack_together = jack_score + jon_score

    # L3
    tom_less_than_jon_jack = 4 # 4 less than the points of Jon and Jack together
    tom_score = jon_jack_together - tom_less_than_jon_jack

    # L4
    total_score = jon_score + jack_score + tom_score

    # FA
    answer = total_score
    return answer