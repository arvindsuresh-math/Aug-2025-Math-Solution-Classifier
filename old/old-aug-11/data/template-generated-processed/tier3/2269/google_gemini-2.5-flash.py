from fractions import Fraction

def solve():
    """Index: 2269.
    Returns: the total number of absent students in the three days.
    """
    # L1
    sick_fraction = Fraction(1, 7) # 1/7 of the total number of students
    total_students = 280 # total number of students in the class is 280
    sick_students_day3 = sick_fraction * total_students

    # L2
    absent_multiplier_day2 = 2 # twice the number of students
    absent_students_day2 = absent_multiplier_day2 * sick_students_day3

    # L3
    present_students_day2 = total_students - absent_students_day2

    # L4
    difference_day2_day1 = 40 # 40 more than the first day
    present_students_day1 = present_students_day2 - difference_day2_day1

    # L5
    absent_students_day1 = total_students - present_students_day1

    # L6
    total_absentees = absent_students_day1 + absent_students_day2 + sick_students_day3

    # FA
    answer = total_absentees
    return answer