from fractions import Fraction

def solve():
    """Index: 7056.
    Returns: the total number of students in all the halls combined.
    """
    # L1
    general_study_hall_students = 30 # 30 students in the general study hall
    biology_multiplier = 2 # twice as many students
    biology_hall_students = biology_multiplier * general_study_hall_students

    # L2
    general_and_biology_total = biology_hall_students + general_study_hall_students

    # L3
    math_hall_fraction = Fraction(3, 5) # 3/5 times as many
    math_hall_students = math_hall_fraction * general_and_biology_total

    # L4
    total_students_all_halls = math_hall_students + general_and_biology_total

    # FA
    answer = total_students_all_halls
    return answer