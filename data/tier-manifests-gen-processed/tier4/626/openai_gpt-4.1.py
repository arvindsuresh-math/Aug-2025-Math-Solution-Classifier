def solve():
    """Index: 626.
    Returns: the number of minutes Jessica will have left when she finishes the exam.
    """
    # L1
    time_used = 12 # She has used 12 minutes of her time
    questions_answered = 16 # She has answered 16 out of 80 questions
    time_per_question = time_used / questions_answered

    # L2
    total_questions = 80 # 80 questions
    total_time_needed = total_questions * time_per_question

    # L3
    total_time_available = 60 # one hour to take an exam
    minutes_left = total_time_available - total_time_needed

    # FA
    answer = minutes_left
    return answer