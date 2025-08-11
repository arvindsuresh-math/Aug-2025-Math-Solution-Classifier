def solve():
    """Index: 6198.
    Returns: the total amount of marks scored by the three students.
    """
    # L1
    keith_score = 3 # Keith scored 3 points
    larry_multiplier = 3 # Larry scored 3 times as many marks
    larry_score = keith_score * larry_multiplier

    # L2
    danny_more_than_larry = 5 # Danny scored 5 more marks than Larry
    danny_score = larry_score + danny_more_than_larry

    # L3
    total_marks = keith_score + larry_score + danny_score

    # FA
    answer = total_marks
    return answer