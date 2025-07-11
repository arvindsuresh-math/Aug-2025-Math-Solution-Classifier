def solve():
    """Index: 1152.
    Returns: the total number of students after adding five more classes.
    """
    # L1
    initial_classes = 15 # 15 classes
    students_per_class = 20 # 20 students per class
    initial_students = initial_classes * students_per_class

    # L2
    added_classes = 5 # added five more classes
    added_students = added_classes * students_per_class

    # L3
    total_students = initial_students + added_students

    # FA
    answer = total_students
    return answer