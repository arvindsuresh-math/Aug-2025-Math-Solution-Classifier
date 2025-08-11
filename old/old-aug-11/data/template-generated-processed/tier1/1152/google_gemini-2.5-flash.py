def solve():
    """Index: 1152.
    Returns: the total number of students in the school.
    """
    # L1
    initial_classes = 15 # 15 classes
    students_per_class = 20 # 20 students per class
    current_students = initial_classes * students_per_class

    # L2
    added_classes = 5 # five more classes
    additional_students = added_classes * students_per_class

    # L3
    total_students = current_students + additional_students

    # FA
    answer = total_students
    return answer