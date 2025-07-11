def solve():
    """Index: 2692.
    Returns: the score Randy should get in the fifth quiz.
    """
    # L1
    desired_average = 94 # 94 average
    num_quizzes_total = 5 # 5 quizzes
    total_sum_needed = desired_average * num_quizzes_total

    # L2
    score1 = 90 # 90
    score2 = 98 # 98
    score3 = 92 # 92
    score4 = 94 # 94
    sum_first_four_quizzes = score1 + score2 + score3 + score4

    # L3
    fifth_quiz_score = total_sum_needed - sum_first_four_quizzes

    # FA
    answer = fifth_quiz_score
    return answer