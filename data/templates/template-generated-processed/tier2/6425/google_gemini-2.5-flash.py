def solve():
    """Index: 6425.
    Returns: the total money Bart earned during these two days.
    """
    # L1
    monday_surveys = 3 # On Monday he finished 3 surveys
    tuesday_surveys = 4 # on Tuesday 4 surveys
    total_surveys = monday_surveys + tuesday_surveys

    # L2
    questions_per_survey = 10 # Each survey has 10 questions
    total_questions = questions_per_survey * total_surveys

    # L3
    pay_per_question = 0.2 # receives $0.2 for every question
    total_earnings = total_questions * pay_per_question

    # FA
    answer = total_earnings
    return answer