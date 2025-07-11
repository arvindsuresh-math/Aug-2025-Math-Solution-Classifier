def solve():
    """Index: 119.
    Returns: the total number of cupcakes Jessa needs to make.
    """
    # L1
    num_fourth_grade_classes = 3 # 3 fourth-grade classes
    students_per_fourth_grade_class = 30 # 30 students
    cupcakes_for_fourth_grade = num_fourth_grade_classes * students_per_fourth_grade_class

    # L2
    cupcakes_for_pe_class = 50 # 50 students
    total_cupcakes = cupcakes_for_fourth_grade + cupcakes_for_pe_class

    # FA
    answer = total_cupcakes
    return answer