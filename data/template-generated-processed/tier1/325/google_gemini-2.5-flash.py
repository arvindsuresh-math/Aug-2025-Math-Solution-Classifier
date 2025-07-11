def solve():
    """Index: 325.
    Returns: the total number of questions Bob created in three hours.
    """
    # L1
    questions_first_hour = 13 # 13 questions in the first hour

    # L2
    doubling_factor = 2 # doubled his rate
    questions_second_hour = questions_first_hour * doubling_factor

    # L3
    questions_third_hour = questions_second_hour * doubling_factor

    # L4
    total_questions = questions_first_hour + questions_second_hour + questions_third_hour

    # FA
    answer = total_questions
    return answer