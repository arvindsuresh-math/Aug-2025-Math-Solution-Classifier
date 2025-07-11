from fractions import Fraction

def solve():
    """Index: 1867.
    Returns: the number of girls on the playground from this class.
    """
    # L1
    total_students = 20 # 20 students in a class
    classroom_fraction = Fraction(1, 4) # one-fourth of the students
    students_in_classroom = total_students * classroom_fraction

    # L2
    students_in_playground = total_students - students_in_classroom

    # L3
    boys_fraction = Fraction(1, 3) # one-third are boys
    boys_in_playground = students_in_playground * boys_fraction

    # L4
    girls_in_playground = students_in_playground - boys_in_playground

    # FA
    answer = girls_in_playground
    return answer