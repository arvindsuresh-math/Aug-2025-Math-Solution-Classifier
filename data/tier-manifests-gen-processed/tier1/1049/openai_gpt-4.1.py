def solve():
    """Index: 1049.
    Returns: Mark's score on the math test.
    """
    # L2
    highest_score = 98 # highest score is 98
    score_range = 75 # range of the scores is 75
    least_score = highest_score - score_range

    # L3
    mark_multiplier = 2 # Mark scored twice as much as the least score
    mark_score = mark_multiplier * least_score

    # FA
    answer = mark_score
    return answer