def solve():
    """Index: 5004.
    Returns: the total number of sheets of paper used for all students.
    """
    # L1
    num_classes = 4 # four classes
    students_per_class = 20 # 20 students each
    total_students = num_classes * students_per_class

    # L2
    sheets_per_student = 5 # 5 sheets of paper per student
    total_sheets = total_students * sheets_per_student

    # FA
    answer = total_sheets
    return answer