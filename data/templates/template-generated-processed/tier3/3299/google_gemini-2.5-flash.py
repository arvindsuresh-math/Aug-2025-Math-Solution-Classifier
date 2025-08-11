def solve():
    """Index: 3299.
    Returns: the number of short-answer questions Karen should assign.
    """
    # L1
    total_homework_hours = 4 # 4 hours of homework total
    minutes_per_hour = 60 # WK
    total_homework_minutes = total_homework_hours * minutes_per_hour

    # L2
    num_essays = 2 # 2 essays
    essay_hours_per_essay = 1 # each essay takes an hour
    total_essay_minutes = num_essays * essay_hours_per_essay * minutes_per_hour

    # L3
    minutes_per_paragraph = 15 # each paragraph takes 15 minutes
    num_paragraphs = 5 # 5 paragraphs
    total_paragraph_minutes = minutes_per_paragraph * num_paragraphs

    # L4
    remaining_minutes_for_short_answer = total_homework_minutes - total_essay_minutes - total_paragraph_minutes

    # L5
    minutes_per_short_answer = 3 # each short-answer question takes 3 minutes
    num_short_answer_questions = remaining_minutes_for_short_answer / minutes_per_short_answer

    # FA
    answer = num_short_answer_questions
    return answer