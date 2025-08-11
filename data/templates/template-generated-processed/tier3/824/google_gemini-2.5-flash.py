from fractions import Fraction

def solve():
    """Index: 824.
    Returns: the total number of students the school can accommodate.
    """
    # L1
    total_classrooms = 15 # A school has 15 classrooms
    fraction_with_30_desks = Fraction(1, 3) # One-third of these classrooms
    classrooms_with_30_desks = fraction_with_30_desks * total_classrooms

    # L2
    classrooms_with_25_desks = total_classrooms - classrooms_with_30_desks

    # L3
    desks_in_30_desk_classrooms = 30 # 30 desks in each classroom
    students_from_30_desk_classrooms = classrooms_with_30_desks * desks_in_30_desk_classrooms

    # L4
    desks_in_25_desk_classrooms = 25 # 25 desks in each classroom
    students_from_25_desk_classrooms = classrooms_with_25_desks * desks_in_25_desk_classrooms

    # L5
    total_students_accommodated = students_from_30_desk_classrooms + students_from_25_desk_classrooms

    # FA
    answer = total_students_accommodated
    return answer