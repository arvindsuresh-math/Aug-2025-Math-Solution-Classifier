def solve():
    """Index: 119.
    Returns: the total number of cupcakes Jessa needs to make.
    """
    # L1
    num_fourth_grade_classes = 3 # 3 fourth-grade classes
    students_per_fourth_grade_class = 30 # each have 30 students
    cupcakes_fourth_grade = num_fourth_grade_classes * students_per_fourth_grade_class

    # L2
    students_pe_class = 50 # P.E. class with 50 students
    total_cupcakes = cupcakes_fourth_grade + students_pe_class

    # FA
    answer = total_cupcakes
    return answer