def solve():
    """Index: 4609.
    Returns: Lizette's average score in her first two quizzes.
    """
    # L1
    average_3_quizzes = 94 # average of 94
    num_quizzes = 3 # average on the 3 quizzes
    total_score_3_quizzes = average_3_quizzes * num_quizzes

    # L2
    score_third_quiz = 92 # scored 92 on her third quiz
    total_score_2_quizzes = total_score_3_quizzes - score_third_quiz

    # L3
    num_first_two_quizzes = 2 # first two quizzes
    average_first_two_quizzes = total_score_2_quizzes / num_first_two_quizzes

    # FA
    answer = average_first_two_quizzes
    return answer