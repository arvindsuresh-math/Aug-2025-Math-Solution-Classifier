from fractions import Fraction

def solve():
    """Index: 133.
    Returns: the number of students in the canteen.
    """
    # L1
    total_students = 40 # 40 students in a class
    absent_fraction = Fraction(1, 10) # 1/10 are absent
    absent_students = total_students * absent_fraction

    # L2
    present_students = total_students - absent_students

    # L3
    classroom_fraction = Fraction(3, 4) # 3/4 of the students who are present are in the classroom
    classroom_students = present_students * classroom_fraction

    # L4
    canteen_students = present_students - classroom_students

    # FA
    answer = canteen_students
    return answer