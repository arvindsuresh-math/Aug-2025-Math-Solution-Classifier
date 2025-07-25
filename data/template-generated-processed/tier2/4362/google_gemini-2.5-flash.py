def solve():
    """Index: 4362.
    Returns: the total number of questions Phillip gets right.
    """
    # L1
    math_total_questions = 40 # The math test has 40 questions
    math_percent_correct_decimal = 0.75 # he gets 75% of them right
    math_correct_questions = math_total_questions * math_percent_correct_decimal

    # L2
    english_total_questions = 50 # The English test has 50 questions
    english_percent_correct_decimal = 0.98 # he gets 98% of them right
    english_correct_questions = english_total_questions * english_percent_correct_decimal

    # L3
    total_correct_questions = math_correct_questions + english_correct_questions

    # FA
    answer = total_correct_questions
    return answer