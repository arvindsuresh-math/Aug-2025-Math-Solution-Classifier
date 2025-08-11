def solve():
    """Index: 5670.
    Returns: the total number of students supposed to be in the class.
    """
    # L1
    students_per_table = 3 # 3 students currently sitting at each table
    num_tables = 6 # 6 tables in the classroom
    current_students = students_per_table * num_tables

    # L2
    girls_to_bathroom = 3 # 3 girls went to the bathroom
    canteen_multiplier = 3 # three times more students went to the canteen
    students_to_canteen = girls_to_bathroom * canteen_multiplier

    # L3
    sally_missing_students = girls_to_bathroom + students_to_canteen

    # L4
    num_new_groups = 2 # 2 groups of students
    students_per_group = 4 # each group has 4 students in it
    elliott_missing_students = num_new_groups * students_per_group

    # L5
    germany_students = 3 # 3 from Germany
    france_students = 3 # 3 from France
    norway_students = 3 # 3 from Norway
    lucas_missing_students = germany_students + france_students + norway_students

    # L6
    total_students = current_students + sally_missing_students + elliott_missing_students + lucas_missing_students

    # FA
    answer = total_students
    return answer