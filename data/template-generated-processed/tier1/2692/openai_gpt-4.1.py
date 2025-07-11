def solve():
    """Index: 2692.
    Returns: the score Randy should get in the fifth quiz to reach a 94 average.
    """
    # L1
    desired_average = 94 # get a 94 average
    total_quizzes = 5 # 5 quizzes
    required_sum = desired_average * total_quizzes

    # L2
    quiz1 = 90 # 90 in his first quiz
    quiz2 = 98 # 98 in his second quiz
    quiz3 = 92 # 92 in his third quiz
    quiz4 = 94 # 94 in his fourth quiz
    sum_first_four = quiz1 + quiz2 + quiz3 + quiz4

    # L3
    fifth_quiz_score = required_sum - sum_first_four

    # FA
    answer = fifth_quiz_score
    return answer