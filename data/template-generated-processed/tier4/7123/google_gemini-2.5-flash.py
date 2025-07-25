def solve():
    """Index: 7123.
    Returns: the number of students in each normal class at the new school.
    """
    # L1
    total_students = 1590 # 1590 students
    transfer_percent = 0.4 # 40% of the students are going to move
    students_to_new_school = total_students * transfer_percent

    # L2
    num_grade_levels = 3 # 3 grade levels
    students_per_grade = students_to_new_school / num_grade_levels

    # L3
    advanced_class_size = 20 # one 20-person advanced class
    students_after_advanced_class = students_per_grade - advanced_class_size

    # L4
    num_additional_classes = 6 # 6 additional classes
    students_per_normal_class = students_after_advanced_class / num_additional_classes

    # FA
    answer = students_per_normal_class
    return answer