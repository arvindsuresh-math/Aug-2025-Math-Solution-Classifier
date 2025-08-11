def solve():
    """Index: 3477.
    Returns: the number of additional volunteers Mr. Johnson needs.
    """
    # L1
    students_per_class = 5 # 5 students from each of the school’s 6 math classes
    num_math_classes = 6 # 6 math classes
    total_student_volunteers = students_per_class * num_math_classes

    # L2
    teacher_volunteers = 13 # 13 teachers have also volunteered
    current_total_volunteers = total_student_volunteers + teacher_volunteers

    # L3
    volunteers_needed = 50 # needs 50 volunteers
    additional_volunteers_needed = volunteers_needed - current_total_volunteers

    # FA
    answer = additional_volunteers_needed
    return answer