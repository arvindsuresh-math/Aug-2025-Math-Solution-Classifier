def solve():
    """Index: 2260.
    Returns: the number of blind students.
    """
    # L1
    blind_students_variable_name = 'x' # Let the number of blind students be x.

    # L2
    deaf_multiplier = 3 # deaf-student population 3 times its blind-student population
    deaf_students_expression = f"{deaf_multiplier}{blind_students_variable_name}"

    # L3
    total_students_given = 180 # 180 students in total
    total_students_equation_left_side = f"{blind_students_variable_name} + {deaf_students_expression}"

    # L4
    combined_coefficient = 1 + deaf_multiplier
    simplified_equation_left_side = f"{combined_coefficient}{blind_students_variable_name}"

    # L5
    blind_students = total_students_given / combined_coefficient

    # FA
    answer = blind_students
    return answer