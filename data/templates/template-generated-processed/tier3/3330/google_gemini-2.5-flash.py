def solve():
    """Index: 3330.
    Returns: the number of pens each student will get.
    """
    # L1
    red_pens_per_student = 62 # 62 red pens
    black_pens_per_student = 43 # 43 black pens
    pens_per_student_initial = red_pens_per_student + black_pens_per_student

    # L2
    number_of_students = 3 # three students
    total_pooled_pens = pens_per_student_initial * number_of_students

    # L3
    pens_taken_first_month = 37 # 37 pens from the pool
    pens_after_first_month = total_pooled_pens - pens_taken_first_month

    # L4
    pens_taken_second_month = 41 # another 41 pens from the pool
    pens_after_second_month = pens_after_first_month - pens_taken_second_month

    # L5
    split_divisor = 3 # split the remaining pens equally among them
    pens_per_student_final = pens_after_second_month / split_divisor

    # FA
    answer = pens_per_student_final
    return answer