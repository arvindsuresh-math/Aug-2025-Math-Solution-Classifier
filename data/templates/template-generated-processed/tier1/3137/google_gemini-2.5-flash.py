def solve():
    """Index: 3137.
    Returns: the minimum score the last student needs to make the teacher happy.
    """
    # L1
    num_students_group1 = 5 # 5 students
    score_group1 = 92 # scored a 92 on the test
    combined_score_group1 = score_group1 * num_students_group1

    # L2
    num_students_group2 = 4 # 4 of which
    score_group2 = 80 # scored an 80
    combined_score_group2 = score_group2 * num_students_group2

    # L3
    combined_score_9_students = combined_score_group1 + combined_score_group2

    # L4
    target_average = 85 # at least 85
    total_students = 10 # 10 students in the class
    required_total_score = target_average * total_students

    # L5
    score_last_student = required_total_score - combined_score_9_students

    # FA
    answer = score_last_student
    return answer