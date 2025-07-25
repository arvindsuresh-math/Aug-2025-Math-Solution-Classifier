def solve():
    """Index: 4573.
    Returns: the total number of students in the classroom.
    """
    # L1
    boys_ratio_part = 3 # The ratio of boys to girls in a classroom is 3:5
    girls_ratio_part = 5 # The ratio of boys to girls in a classroom is 3:5
    total_ratio_parts = boys_ratio_part + girls_ratio_part

    # L2
    difference_in_parts = girls_ratio_part - boys_ratio_part

    # L3
    more_girls_students = 4 # 4 more girls than boys
    students_per_part = more_girls_students / difference_in_parts

    # L4
    total_students = total_ratio_parts * students_per_part

    # FA
    answer = total_students
    return answer