def solve():
    """Index: 6602.
    Returns: the total number of incorrect answers the team got.
    """
    # L1
    total_questions = 35 # Out of the 35 questions
    riley_mistakes = 3 # Riley got 3 mistakes
    riley_score = total_questions - riley_mistakes

    # L2
    half_divisor = 2 # half the score of Riley
    half_riley_score = riley_score / half_divisor

    # L3
    ofelia_score_additional = 5 # 5 more than half the score of Riley
    ofelia_score = half_riley_score + ofelia_score_additional

    # L4
    ofelia_incorrect_answers = total_questions - ofelia_score

    # L5
    team_incorrect_answers = riley_mistakes + ofelia_incorrect_answers

    # FA
    answer = team_incorrect_answers
    return answer