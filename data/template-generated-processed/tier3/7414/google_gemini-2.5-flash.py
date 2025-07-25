from fractions import Fraction

def solve():
    """Index: 7414.
    Returns: the number of students in the third group.
    """
    # L1
    total_students = 45 # class of 45 students
    first_group_fraction = Fraction(1, 3) # a third of the class
    first_group_students = first_group_fraction * total_students

    # L2
    remaining_students_after_first_group = total_students - first_group_students

    # L3
    second_group_fraction = Fraction(2, 5) # two-fifths are above 11 but under 13
    second_group_students = second_group_fraction * total_students

    # L4
    third_group_students = remaining_students_after_first_group - second_group_students

    # FA
    answer = third_group_students
    return answer