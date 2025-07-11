def solve():
    """Index: 2679.
    Returns: the average bowling score of Gretchen, Mitzi, and Beth.
    """
    # L1
    gretchen_score = 120 # Gretchen bowled a 120
    mitzi_score = 113 # Mitzi bowled a 113
    beth_score = 85 # Beth bowled an 85
    combined_score = gretchen_score + mitzi_score + beth_score

    # L2
    num_bowlers = 3 # Gretchen, Mitzi, and Beth
    average_score = combined_score / num_bowlers

    # FA
    answer = average_score
    return answer