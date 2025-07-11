def solve():
    """Index: 1216.
    Returns: the number of desserts each student gets.
    """
    # L1
    mini_cupcakes = 14 # 14 mini-cupcakes
    donut_holes = 12 # 12 donut holes
    total_desserts = mini_cupcakes + donut_holes

    # L2
    num_students = 13 # 13 students
    desserts_per_student = total_desserts / num_students

    # FA
    answer = desserts_per_student
    return answer