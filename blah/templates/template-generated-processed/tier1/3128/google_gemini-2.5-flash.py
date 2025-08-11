def solve():
    """Index: 3128.
    Returns: the total number of students who went on the field trip.
    """
    # L1
    num_vans = 6 # six vans
    students_per_van = 10 # 10 students on each van
    students_from_vans = num_vans * students_per_van

    # L2
    num_minibuses = 4 # four minibusses
    students_per_minibus = 24 # 24 students on each minibus
    students_from_minibuses = num_minibuses * students_per_minibus

    # L3
    total_students = students_from_vans + students_from_minibuses

    # FA
    answer = total_students
    return answer