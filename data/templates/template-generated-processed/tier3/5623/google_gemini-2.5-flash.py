from fractions import Fraction

def solve():
    """Index: 5623.
    Returns: the number of students who don't have a favorite subject.
    """
    # L1
    total_students = 30 # In a class of 30 students
    math_fraction = Fraction(1, 5) # 1/5 of the students like Math
    math_students = total_students * math_fraction

    # L2
    english_fraction = Fraction(1, 3) # 1/3 like English
    english_students = total_students * english_fraction

    # L3
    math_english_students = math_students + english_students

    # L4
    remaining_students_after_math_english = total_students - math_english_students

    # L5
    science_fraction = Fraction(1, 7) # 1/7 of the remaining students like Science
    science_students = remaining_students_after_math_english * science_fraction

    # L6
    no_favorite_subject_students = remaining_students_after_math_english - science_students

    # FA
    answer = no_favorite_subject_students
    return answer