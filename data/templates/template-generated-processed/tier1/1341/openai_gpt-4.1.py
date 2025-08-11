def solve():
    """Index: 1341.
    Returns: the number of questions Sasha still needs to complete after 2 hours.
    """
    # L1
    questions_per_hour = 15 # Sasha can complete 15 questions an hour
    hours_worked = 2 # she works for 2 hours
    questions_completed = questions_per_hour * hours_worked

    # L2
    total_questions = 60 # she has 60 questions to complete
    questions_left = total_questions - questions_completed

    # FA
    answer = questions_left
    return answer