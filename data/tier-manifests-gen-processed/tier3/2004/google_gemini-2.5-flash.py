def solve():
    """Index: 2004.
    Returns: the marks Jake scored in the third test.
    """
    # L1
    num_tests = 4 # four tests
    average_score = 75 # average of marks scored in four tests by Jake was 75
    total_marks_four_tests = num_tests * average_score

    # L2
    first_test_score = 80 # 80 marks in the first test
    second_test_increase = 10 # 10 more in the second test
    second_test_score = first_test_score + second_test_increase

    # L3
    combined_first_second_test_marks = second_test_score + first_test_score

    # L4
    combined_third_fourth_test_marks = total_marks_four_tests - combined_first_second_test_marks

    # L5
    num_equal_tests = 2 # third and fourth test
    third_test_score = combined_third_fourth_test_marks / num_equal_tests

    # FA
    answer = third_test_score
    return answer