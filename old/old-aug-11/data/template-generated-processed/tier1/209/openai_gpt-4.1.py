def solve():
    """Index: 209.
    Returns: the number of girls among the students on the field trip.
    """
    # L1
    num_vans = 5 # Five coaster vans
    students_per_van = 28 # Each van carries 28 students
    total_students = num_vans * students_per_van

    # L2
    num_boys = 60 # 60 of which are boys
    num_girls = total_students - num_boys

    # FA
    answer = num_girls
    return answer