def solve():
    """Index: 2337.
    Returns: the total amount the P.T.O. spent on shirts.
    """
    # L1
    kinder_students = 101 # 101 Kindergartners
    kinder_shirt_cost = 5.80 # $5.80 each
    kinder_total_cost = kinder_students * kinder_shirt_cost

    # L2
    first_grade_students = 113 # 113 first graders
    first_grade_shirt_cost = 5 # $5 each
    first_grade_total_cost = first_grade_students * first_grade_shirt_cost

    # L3
    second_grade_students = 107 # 107 second graders
    second_grade_shirt_cost = 5.60 # $5.60 each
    second_grade_total_cost = second_grade_students * second_grade_shirt_cost

    # L4
    third_grade_students = 108 # 108 third graders
    third_grade_shirt_cost = 5.25 # $5.25 each
    third_grade_total_cost = third_grade_students * third_grade_shirt_cost

    # L5
    total_cost = kinder_total_cost + first_grade_total_cost + second_grade_total_cost + third_grade_total_cost

    # FA
    answer = total_cost
    return answer