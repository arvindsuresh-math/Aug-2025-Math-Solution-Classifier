def solve():
    """Index: 3785.
    Returns: the percentage needed on the third math test.
    """
    # L3
    first_test_score = 95 # 95% on her first math test
    second_test_score = 80 # 80% on her second math test
    desired_average = 90 # average grade of at least 90%
    num_tests = 3 # three tests
    sum_of_scores_needed = desired_average * num_tests

    # L4
    third_test_score = sum_of_scores_needed - first_test_score - second_test_score

    # L5
    # This line confirms the value of x calculated in the previous step.
    # No new computation is performed here, just a restatement of the result.
    # The variable 'third_test_score' already holds the final value.

    # FA
    answer = third_test_score
    return answer