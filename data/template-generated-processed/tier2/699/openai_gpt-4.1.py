def solve():
    """Index: 699.
    Returns: the total cost for one lunch for all the students.
    """
    # L1
    num_third_grade_classes = 5 # 5 third grade classes
    students_per_third_grade_class = 30 # 30 students each
    total_third_grade_students = num_third_grade_classes * students_per_third_grade_class

    # L2
    num_fourth_grade_classes = 4 # 4 fourth grade classes
    students_per_fourth_grade_class = 28 # 28 students each
    total_fourth_grade_students = num_fourth_grade_classes * students_per_fourth_grade_class

    # L3
    num_fifth_grade_classes = 4 # 4 fifth grade classes
    students_per_fifth_grade_class = 27 # 27 students each
    total_fifth_grade_students = num_fifth_grade_classes * students_per_fifth_grade_class

    # L4
    total_students = total_third_grade_students + total_fourth_grade_students + total_fifth_grade_students

    # L5
    hamburger_cost = 2.10 # hamburger, which costs $2.10
    carrots_cost = 0.50 # carrots, which cost $0.50
    cookie_cost = 0.20 # cookie, which cost $0.20
    lunch_cost_per_student = hamburger_cost + carrots_cost + cookie_cost

    # L6
    total_lunch_cost = lunch_cost_per_student * total_students

    # FA
    answer = total_lunch_cost
    return answer