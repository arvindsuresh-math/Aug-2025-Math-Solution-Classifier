def solve():
    """Index: 6654.
    Returns: the total number of packs John bought according to the solution's interpretation.
    """
    # L1
    num_classes = 6 # 6 classes
    students_per_class = 30 # 30 students in each class
    total_students = num_classes * students_per_class

    # L2
    packs_per_student = 2 # 2 packs of index cards for all his students (interpreted as per student by the solution)
    total_packs = total_students * packs_per_student

    # FA
    answer = total_packs
    return answer