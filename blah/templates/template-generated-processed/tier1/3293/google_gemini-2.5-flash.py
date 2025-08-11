def solve():
    """Index: 3293.
    Returns: the minimum grade Carl needs on his last test to achieve an 85 average.
    """
    # L1
    desired_average = 85 # an 85 average
    num_tests = 4 # four tests
    total_needed_points = desired_average * num_tests

    # L2
    test1_score = 80 # got an 80
    test2_score = 75 # a 75
    test3_score = 90 # a 90
    last_test_score = total_needed_points - test1_score - test2_score - test3_score

    # FA
    answer = last_test_score
    return answer