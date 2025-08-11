def solve():
    """Index: 3570.
    Returns: the grade Brittany got on her second test.
    """
    # L1
    average_grade_after_second_test = 81 # her average rose to an 81
    num_tests_after_second = 2 # after her second test
    total_points_after_second = average_grade_after_second_test * num_tests_after_second

    # L2
    grade_first_test = 78 # got a 78 on her first test
    grade_second_test = total_points_after_second - grade_first_test

    # FA
    answer = grade_second_test
    return answer