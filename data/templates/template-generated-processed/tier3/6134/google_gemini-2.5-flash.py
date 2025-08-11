from fractions import Fraction

def solve():
    """Index: 6134.
    Returns: the total number of eyes that saw the airplane.
    """
    # L1
    total_students = 200 # 200 students
    fraction_looked_up = Fraction(3, 4) # 3/4 of the students
    students_looked_up = fraction_looked_up * total_students

    # L2
    eyes_per_student = 2 # each student has two eyes
    total_eyes = eyes_per_student * students_looked_up

    # FA
    answer = total_eyes
    return answer