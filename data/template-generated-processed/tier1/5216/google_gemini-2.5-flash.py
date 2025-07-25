def solve():
    """Index: 5216.
    Returns: the score Jacob must earn on his fifth test to have an overall average of 85.
    """
    # L1
    desired_average = 85 # an overall average of 85
    num_tests = 5 # five tests
    total_points_needed = desired_average * num_tests

    # L2
    test1_score = 85 # earns 85
    test2_score = 79 # 79
    test3_score = 92 # 92
    test4_score = 84 # and 84
    current_points = test1_score + test2_score + test3_score + test4_score

    # L3
    fifth_test_score_needed = total_points_needed - current_points

    # FA
    answer = fifth_test_score_needed
    return answer