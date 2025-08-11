from fractions import Fraction

def solve():
    """Index: 3596.
    Returns: the total number of students in the class.
    """
    # L1
    students_brown_eyes_black_hair = 6 # 6 students in the class with brown eyes and black hair
    half_inverse_multiplier = 2 # WK
    students_with_brown_eyes = students_brown_eyes_black_hair * half_inverse_multiplier

    # L2
    two_thirds_inverse = Fraction(3, 2) # WK
    total_students = students_with_brown_eyes * two_thirds_inverse

    # FA
    answer = total_students
    return answer