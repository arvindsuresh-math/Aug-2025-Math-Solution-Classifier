def solve():
    """Index: 2789.
    Returns: the score Maria needs on her fourth test to average 85.
    """
    # L1
    num_tests = 4 # four tests
    desired_average = 85 # average score for the four tests is exactly 85
    total_needed = num_tests * desired_average

    # L2
    score1 = 80 # 80
    score2 = 70 # 70
    score3 = 90 # 90
    current_total = score1 + score2 + score3

    # L3
    needed_fourth_score = total_needed - current_total

    # FA
    answer = needed_fourth_score
    return answer