def solve():
    """Index: 1752.
    Returns: the total combined score of Meghan, Jose, and Alisson in the test.
    """
    # L1
    num_questions = 50 # 50-question test
    marks_per_question = 2 # two marks for each question
    total_possible_marks = num_questions * marks_per_question

    # L2
    jose_wrong = 5 # Jose got 5 questions wrong
    jose_marks_lost = jose_wrong * marks_per_question

    # L3
    jose_score = total_possible_marks - jose_marks_lost

    # L4
    meghan_less_than_jose = 20 # Meghan scored 20 marks less than Jose
    meghan_score = jose_score - meghan_less_than_jose

    # L5
    jose_meghan_total = meghan_score + jose_score

    # L6
    alisson_less_than_jose = 40 # Jose scored 40 more marks than Alisson
    alisson_score = jose_score - alisson_less_than_jose

    # L7
    answer = jose_meghan_total + alisson_score
    return answer