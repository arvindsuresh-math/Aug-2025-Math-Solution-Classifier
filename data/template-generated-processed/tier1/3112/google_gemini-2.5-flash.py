def solve():
    """Index: 3112.
    Returns: the total number of students who shook the mayor's hand.
    """
    # L1
    third_school_students = 200 # third school had 200 students
    second_school_more_than_third = 40 # second school had 40 more students than the third school
    second_school_students = third_school_students + second_school_more_than_third

    # L2
    third_and_second_school_total = second_school_students + third_school_students

    # L3
    first_school_multiplier = 2 # twice as many students
    first_school_students = second_school_students * first_school_multiplier

    # L4
    total_students_shook_hand = first_school_students + third_and_second_school_total

    # FA
    answer = total_students_shook_hand
    return answer