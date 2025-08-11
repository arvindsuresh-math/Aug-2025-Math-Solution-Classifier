def solve():
    """Index: 2596.
    Returns: the total score across all 4 subjects.
    """
    # L1
    geography_score = 50 # Henry scored 50 points on his Geography test
    math_score = 70 # 70 on his Math test
    english_score = 66 # and 66 on his English test
    sum_of_first_three_scores = geography_score + math_score + english_score

    # L2
    number_of_subjects = 3 # average of these 3 scores
    history_score = sum_of_first_three_scores / number_of_subjects

    # L3
    total_score_all_subjects = sum_of_first_three_scores + history_score

    # FA
    answer = total_score_all_subjects
    return answer