def solve():
    """Index: 5934.
    Returns: the total number of math students Ms. Cole teaches.
    """
    # L1
    students_sixth_level = 40 # sixth-level class has 40 students
    multiplier_fourth_level = 4 # four times as many students in Ms. Cole's fourth-level math class
    students_fourth_level = multiplier_fourth_level * students_sixth_level

    # L2
    students_fourth_and_sixth_level = students_fourth_level + students_sixth_level

    # L3
    multiplier_seventh_level = 2 # twice that in the fourth-level math class
    students_seventh_level = multiplier_seventh_level * students_fourth_level

    # L4
    total_students = students_seventh_level + students_fourth_and_sixth_level

    # FA
    answer = total_students
    return answer