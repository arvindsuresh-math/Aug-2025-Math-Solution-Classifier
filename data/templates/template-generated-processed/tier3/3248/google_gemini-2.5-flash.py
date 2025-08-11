from fractions import Fraction

def solve():
    """Index: 3248.
    Returns: the number of students who passed their finals.
    """
    # L1
    total_students = 180 # 180 students in ninth grade
    breakup_fraction = Fraction(1, 4) # 1/4 of them bombed their finals
    students_with_breakups = breakup_fraction * total_students

    # L2
    remaining_students_after_breakups = total_students - students_with_breakups

    # L3
    no_show_denominator = 3 # 1/3rd of the rest didn't show up
    students_no_show = remaining_students_after_breakups / no_show_denominator

    # L4
    failed_less_than_D = 20 # another 20 got less than a D
    students_passed = total_students - students_with_breakups - students_no_show - failed_less_than_D

    # FA
    answer = students_passed
    return answer