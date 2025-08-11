def solve():
    """Index: 3321.
    Returns: the total number of questions John got right.
    """
    # L1
    first_part_questions = 40 # first 40 questions
    first_part_correct_percent = 0.9 # 90% right
    first_part_correct_count = first_part_questions * first_part_correct_percent

    # L2
    second_part_questions = 40 # next 40 questions
    second_part_correct_percent = 0.95 # 95% right
    second_part_correct_count = second_part_questions * second_part_correct_percent

    # L3
    total_correct_questions = first_part_correct_count + second_part_correct_count

    # FA
    answer = total_correct_questions
    return answer