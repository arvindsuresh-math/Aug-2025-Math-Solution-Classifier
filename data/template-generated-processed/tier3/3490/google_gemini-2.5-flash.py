def solve():
    """Index: 3490.
    Returns: the number of unanswered questions.
    """
    # L1
    hours_spent = 2 # 2 hours
    minutes_per_hour = 60 # Each hour contains 60 minutes
    total_minutes_spent = hours_spent * minutes_per_hour

    # L2
    minutes_per_question = 2 # two minutes for each answer
    questions_answered = total_minutes_spent / minutes_per_question

    # L3
    total_questions = 100 # 100 questions on a test
    unanswered_questions = total_questions - questions_answered

    # FA
    answer = unanswered_questions
    return answer