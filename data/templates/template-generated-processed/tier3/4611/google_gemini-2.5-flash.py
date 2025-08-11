from fractions import Fraction

def solve():
    """Index: 4611.
    Returns: the number of students in the class at the end of the year.
    """
    # L1
    initial_students = 160 # number of students that were in Hendrix's class before 20 new students joined was 160
    new_students = 20 # 20 new students
    students_after_joining = initial_students + new_students

    # L2
    transfer_fraction = Fraction(1, 3) # 1/3 of the students
    transferred_students = transfer_fraction * students_after_joining

    # L3
    remaining_students = students_after_joining - transferred_students

    # FA
    answer = remaining_students
    return answer