from fractions import Fraction

def solve():
    """Index: 6919.
    Returns: the combined total number of students who like history and maths.
    """
    # L1
    total_students = 25 # 25 students
    math_fraction = Fraction(2, 5) # 2/5 of the students like maths
    students_like_maths = math_fraction * total_students

    # L2
    students_not_math = total_students - students_like_maths

    # L3
    science_fraction = Fraction(1, 3) # 1/3 of the remaining students like science
    students_like_science = science_fraction * students_not_math

    # L4
    students_like_history = students_not_math - students_like_science

    # L5
    combined_total = students_like_history + students_like_maths

    # FA
    answer = combined_total
    return answer