def solve():
    """Index: 5873.
    Returns: the total number of students in each classroom.
    """
    # L1
    total_boys = 56 # 56 boys
    num_classrooms = 4 # 4 classrooms
    boys_per_classroom = total_boys / num_classrooms

    # L2
    total_girls = 44 # 44 girls
    girls_per_classroom = total_girls / num_classrooms

    # L3
    total_students_per_classroom = boys_per_classroom + girls_per_classroom

    # FA
    answer = total_students_per_classroom
    return answer