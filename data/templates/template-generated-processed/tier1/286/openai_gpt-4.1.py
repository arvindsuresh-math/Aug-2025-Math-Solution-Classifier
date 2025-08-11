def solve():
    """Index: 286.
    Returns: the number of girls who were not able to join the field trip.
    """
    # L1
    boys = 8 # Eight of these students were boys
    girls = 18 - boys # 18 students assigned in a minibus for a field trip
    girls_joined = boys # the number of girls and boys was the same
    students_joined = boys + girls_joined

    # L2
    total_students = 18 # 18 students assigned in a minibus for a field trip
    girls_not_joined = total_students - students_joined

    # FA
    answer = girls_not_joined
    return answer