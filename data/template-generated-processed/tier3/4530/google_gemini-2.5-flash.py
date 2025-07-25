def solve():
    """Index: 4530.
    Returns: Marion's score.
    """
    # L1
    total_items_exam = 40 # 40-item Statistics exam
    ella_incorrect_answers = 4 # Ella got 4 incorrect answers
    ella_score = total_items_exam - ella_incorrect_answers

    # L2
    divisor_half = 2 # half the score of Ella
    half_ella_score = ella_score / divisor_half

    # L3
    marion_additional_score = 6 # Marion got 6 more
    marion_score = half_ella_score + marion_additional_score

    # FA
    answer = marion_score
    return answer