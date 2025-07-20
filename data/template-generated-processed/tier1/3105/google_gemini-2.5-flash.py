def solve():
    """Index: 3105.
    Returns: the total number of students that can be seated on the bus.
    """
    # L1
    num_rows = 13 # 13 rows of seats
    sections_per_row = 2 # two sections
    total_sections = num_rows * sections_per_row

    # L2
    students_per_section = 2 # two students to sit in each section
    total_students = total_sections * students_per_section

    # FA
    answer = total_students
    return answer