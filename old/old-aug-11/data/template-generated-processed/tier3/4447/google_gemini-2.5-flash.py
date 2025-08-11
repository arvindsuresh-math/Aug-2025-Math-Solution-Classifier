def solve():
    """Index: 4447.
    Returns: the total number of hours Martiza needs to study.
    """
    # L1
    num_multiple_choice_questions = 30 # 30 are multiple-choice
    time_per_mc_question = 15 # 15 minutes to learn each multiple-choice question
    total_mc_minutes = num_multiple_choice_questions * time_per_mc_question

    # L2
    time_per_fib_question = 25 # 25 minutes each to learn the fill-in-the-blank questions
    num_fib_questions = 30 # 30 are fill-in-the-blank
    total_fib_minutes = time_per_fib_question * num_fib_questions

    # L3
    total_study_minutes = total_mc_minutes + total_fib_minutes

    # L4
    minutes_per_hour = 60 # WK
    total_study_hours = total_study_minutes / minutes_per_hour

    # FA
    answer = total_study_hours
    return answer