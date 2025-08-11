def solve():
    """Index: 2789.
    Returns: the score Maria needs on the fourth test.
    """
    # L1
    num_tests = 4 # four tests
    desired_average_score = 85 # average score for the four tests is exactly 85
    total_desired_score = num_tests * desired_average_score

    # L2
    score1 = 80 # test scores are 80
    score2 = 70 # test scores are 70
    score3 = 90 # test scores are 90
    current_total_score = score1 + score2 + score3

    # L3
    score_needed_fourth_test = total_desired_score - current_total_score

    # FA
    answer = score_needed_fourth_test
    return answer