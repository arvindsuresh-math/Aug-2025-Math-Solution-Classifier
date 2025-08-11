def solve():
    """Index: 5768.
    Returns: the score Amanda needs on the final quiz to get an A.
    """
    # L1
    num_quizzes_initial = 4 # taken 4 quizzes
    avg_score_initial = 92 # averaged a 92% score
    total_points_initial = num_quizzes_initial * avg_score_initial

    # L2
    total_quizzes = 5 # 5 quizzes
    required_avg_score = 93 # average 93%
    required_total_points = total_quizzes * required_avg_score

    # L3
    score_needed_final_quiz = required_total_points - total_points_initial

    # FA
    answer = score_needed_final_quiz
    return answer