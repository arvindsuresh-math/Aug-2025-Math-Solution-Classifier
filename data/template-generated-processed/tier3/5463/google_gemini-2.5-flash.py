def solve():
    """Index: 5463.
    Returns: the total number of cans collected by Ms. Perez's class.
    """
    # L1
    total_students = 30 # Ms. Perez's class has 30 students
    half_divisor = 2 # Half the students
    students_collected_12_cans = total_students / half_divisor

    # L2
    cans_per_student_12 = 12 # collected 12 cans each
    total_cans_from_12_can_collectors = students_collected_12_cans * cans_per_student_12

    # L3
    remaining_students = 13 # the remaining 13 students
    cans_per_student_4 = 4 # each collected 4 cans
    total_cans_from_4_can_collectors = remaining_students * cans_per_student_4

    # L4
    total_cans_collected = total_cans_from_12_can_collectors + total_cans_from_4_can_collectors

    # FA
    answer = total_cans_collected
    return answer