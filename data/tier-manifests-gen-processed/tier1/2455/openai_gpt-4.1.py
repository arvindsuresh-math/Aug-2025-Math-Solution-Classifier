def solve():
    """Index: 2455.
    Returns: the total cost of supplies for the class.
    """
    # L1
    bow_cost = 5 # Bows are $5 each
    vinegar_cost = 2 # a bottle of vinegar is $2
    baking_soda_cost = 1 # a box of baking soda is $1
    per_student_cost = bow_cost + vinegar_cost + baking_soda_cost

    # L2
    num_students = 23 # 23 students in this class
    total_cost = per_student_cost * num_students

    # FA
    answer = total_cost
    return answer