def solve():
    """Index: 286.
    Returns: the number of girls who were not able to join the field trip.
    """
    # L1
    boys_on_trip = 8 # Eight of these students were boys
    girls_on_trip = 8 # the number of girls and boys was the same
    students_joined_trip = boys_on_trip + girls_on_trip

    # L2
    total_students_assigned = 18 # 18 students assigned in a minibus
    girls_not_able_to_join = total_students_assigned - students_joined_trip

    # FA
    answer = girls_not_able_to_join
    return answer