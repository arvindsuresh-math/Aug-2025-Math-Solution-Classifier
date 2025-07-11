def solve():
    """Index: 1341.
    Returns: the number of questions Sasha still needs to complete.
    """
    # L1
    questions_per_hour = 15 # 15 questions an hour
    hours_worked = 2 # works for 2 hours
    questions_completed = questions_per_hour * hours_worked

    # L2
    total_questions = 60 # 60 questions to complete
    questions_remaining = total_questions - questions_completed

    # FA
    answer = questions_remaining
    return answer