from fractions import Fraction

def solve():
    """Index: 7165.
    Returns: the number of students still in school.
    """
    # L1
    total_students = 1000 # A school has 1000 students
    fraction_taken_to_beach = Fraction(1, 2) # Half of the students
    students_taken_to_beach = total_students * fraction_taken_to_beach

    # L2
    students_not_taken_to_beach = total_students - students_taken_to_beach

    # L3
    fraction_sent_home = Fraction(1, 2) # Half of the remaining students
    students_sent_home = fraction_sent_home * students_not_taken_to_beach

    # L4
    students_still_in_school = students_not_taken_to_beach - students_sent_home

    # FA
    answer = students_still_in_school
    return answer