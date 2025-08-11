def solve():
    """Index: 5344.
    Returns: the total number of students altogether.
    """
    # L1
    multiplier_skiing = 2 # twice as many
    students_scavenger_hunt = 4000 # 4000 students who wish to go on the scavenger hunting trip
    students_skiing_trip = multiplier_skiing * students_scavenger_hunt

    # L2
    total_students = students_scavenger_hunt + students_skiing_trip

    # FA
    answer = total_students
    return answer