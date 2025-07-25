def solve():
    """Index: 3516.
    Returns: the amount each student will contribute.
    """
    # L1
    total_contribution_needed = 90 # each class will contribute $90
    class_funds = 14 # has $14 class funds
    remaining_amount_to_divide = total_contribution_needed - class_funds

    # L2
    number_of_students = 19 # among 19 students
    contribution_per_student = remaining_amount_to_divide / number_of_students

    # FA
    answer = contribution_per_student
    return answer