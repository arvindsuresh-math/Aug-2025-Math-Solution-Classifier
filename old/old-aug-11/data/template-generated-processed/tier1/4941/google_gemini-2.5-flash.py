def solve():
    """Index: 4941.
    Returns: the total amount of money raised by the students.
    """
    # L1
    amount_per_student_group1 = 20 # raised $20 each
    num_students_group1 = 10 # Ten of the students
    total_raised_group1 = amount_per_student_group1 * num_students_group1

    # L2
    total_students = 30 # Thirty students
    num_students_group2 = total_students - num_students_group1

    # L3
    amount_per_student_group2 = 30 # raised $30 each
    total_raised_group2 = amount_per_student_group2 * num_students_group2

    # L4
    total_raised_all_students = total_raised_group1 + total_raised_group2

    # FA
    answer = total_raised_all_students
    return answer