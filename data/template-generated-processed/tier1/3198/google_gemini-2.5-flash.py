def solve():
    """Index: 3198.
    Returns: the total number of questions asked in the competition.
    """
    # L1
    drew_correct_questions = 20 # Drew got 20 questions correct
    drew_wrong_questions = 6 # six questions wrong
    drew_total_questions = drew_correct_questions + drew_wrong_questions

    # L2
    multiplier_twice = 2 # twice as many questions wrong
    carla_wrong_questions = multiplier_twice * drew_wrong_questions

    # L3
    carla_correct_questions = 14 # Carla got 14 questions correct
    carla_total_questions = carla_wrong_questions + carla_correct_questions

    # L4
    total_questions_asked = drew_total_questions + carla_total_questions

    # FA
    answer = total_questions_asked
    return answer