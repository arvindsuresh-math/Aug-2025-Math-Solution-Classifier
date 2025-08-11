def solve():
    """Index: 6881.
    Returns: the number of multiple-choice questions.
    """
    # L1
    total_percentage = 100 # WK
    problem_solving_percentage = 80 # 80% of the 50 questions are problem-solving
    multiple_choice_percentage_value = total_percentage - problem_solving_percentage

    # L2
    total_questions = 50 # 50 questions
    percentage_divisor = 100 # WK
    num_multiple_choice_questions = total_questions * multiple_choice_percentage_value / percentage_divisor

    # FA
    answer = num_multiple_choice_questions
    return answer