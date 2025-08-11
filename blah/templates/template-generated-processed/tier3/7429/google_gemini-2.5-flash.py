from fractions import Fraction

def solve():
    """Index: 7429.
    Returns: the number of students present.
    """
    # L1
    total_students = 28 # 28 students in a class
    absent_fraction = Fraction(2, 7) # Two-sevenths of them were absent
    absent_students = total_students * absent_fraction

    # L2
    present_students = total_students - absent_students

    # FA
    answer = present_students
    return answer