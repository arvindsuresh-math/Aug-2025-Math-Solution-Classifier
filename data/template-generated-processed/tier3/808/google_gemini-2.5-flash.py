from fractions import Fraction

def solve():
    """Index: 808.
    Returns: the total number of students Carla teaches.
    """
    # L1
    students_in_restroom = 2 # 2 students are in the restroom
    multiplier_absent = 3 # three times that number
    subtractor_absent = 1 # one less than
    absent_students = students_in_restroom * multiplier_absent - subtractor_absent

    # L2
    desks_per_row = 6 # six desks each
    fraction_full = Fraction(2, 3) # 2/3 full
    students_per_row = desks_per_row * fraction_full

    # L3
    num_rows = 4 # four rows
    students_in_rows = num_rows * students_per_row

    # L4
    total_students_carla_teaches = students_in_rows + students_in_restroom + absent_students

    # FA
    answer = total_students_carla_teaches
    return answer