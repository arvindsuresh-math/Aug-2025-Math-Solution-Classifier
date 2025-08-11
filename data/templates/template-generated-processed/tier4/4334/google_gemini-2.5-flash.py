def solve():
    """Index: 4334.
    Returns: the difference in minutes Joan has for each question on the Math exam compared to the English exam.
    """
    # L1
    english_exam_hours = 1 # 1 hour
    minutes_per_hour = 60 # WK
    english_exam_minutes = english_exam_hours * minutes_per_hour

    # L2
    english_questions = 30 # 30 questions
    time_per_english_question = english_exam_minutes / english_questions

    # L3
    math_exam_hours = 1.5 # 1.5 hours
    math_exam_minutes = math_exam_hours * minutes_per_hour

    # L4
    math_questions = 15 # 15 questions
    time_per_math_question = math_exam_minutes / math_questions

    # L5
    time_difference = time_per_math_question - time_per_english_question

    # FA
    answer = time_difference
    return answer