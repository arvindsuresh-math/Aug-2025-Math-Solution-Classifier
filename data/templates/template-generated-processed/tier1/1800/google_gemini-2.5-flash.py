def solve():
    """Index: 1800.
    Returns: Madeline's score in the Geometry exam.
    """
    # L1
    madeline_mistakes = 2 # Madeline got 2 mistakes
    multiplier_for_leo = 2 # half as many mistakes as Leo
    leo_mistakes = madeline_mistakes * multiplier_for_leo

    # L2
    brent_more_mistakes_than_leo = 1 # 1 more mistake than Leo
    brent_mistakes = leo_mistakes + brent_more_mistakes_than_leo

    # L3
    brent_score = 25 # Brent scored 25
    perfect_score = brent_score + brent_mistakes

    # L4
    madeline_score = perfect_score - madeline_mistakes

    # FA
    answer = madeline_score
    return answer