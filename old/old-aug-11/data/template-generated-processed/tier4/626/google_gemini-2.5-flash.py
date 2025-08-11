def solve():
    """Index: 626.
    Returns: the number of minutes left when she finishes the exam.
    """
    # L1
    minutes_used = 12 # She has used 12 minutes of her time
    questions_answered = 16 # She has answered 16 out of 80 questions
    time_per_question = minutes_used / questions_answered

    # L2
    total_questions = 80 # 80 questions
    total_time_needed = total_questions * time_per_question

    # L3
    allotted_time_in_minutes = 60 # Jessica has one hour to take an exam
    minutes_left = allotted_time_in_minutes - total_time_needed

    # FA
    answer = minutes_left
    return answer