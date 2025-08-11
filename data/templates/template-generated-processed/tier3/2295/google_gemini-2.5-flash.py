def solve():
    """Index: 2295.
    Returns: the number of couples who came to the prom.
    """
    # L1
    total_students = 123 # 123 students who attended
    single_attendees = 3 # 3 students attended on their own
    students_in_couples = total_students - single_attendees

    # L2
    students_per_couple = 2 # WK
    number_of_couples = students_in_couples / students_per_couple

    # FA
    answer = number_of_couples
    return answer