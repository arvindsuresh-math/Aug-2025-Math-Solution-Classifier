def solve():
    """Index: 7193.
    Returns: the number of questions Hannah needs to get right.
    """
    # L1
    total_questions = 40 # 40
    wrong_questions = 3 # 3 wrong out of 40
    student1_right_questions = total_questions - wrong_questions

    # L2
    student1_proportion_right = student1_right_questions / total_questions

    # L3
    percent_multiplier = 100 # WK
    student1_percentage = student1_proportion_right * percent_multiplier

    # L4
    student2_percentage_value = 95 # 95% on the exam
    student2_percentage_decimal = 0.95 # 95% on the exam
    student2_right_questions = total_questions * student2_percentage_decimal

    # L6
    score_to_beat_plus_one = 1 # 38 + 1
    hannah_required_score = student2_right_questions + score_to_beat_plus_one

    # FA
    answer = hannah_required_score
    return answer