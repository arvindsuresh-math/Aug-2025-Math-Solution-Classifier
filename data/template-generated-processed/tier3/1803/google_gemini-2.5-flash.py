from fractions import Fraction

def solve():
    """Index: 1803.
    Returns: the number of students now in the cafeteria.
    """
    # L1
    total_students = 90 # 90 students
    cafeteria_fraction = Fraction(2, 3) # two-thirds of the students sat in the cafeteria
    original_cafeteria_students = total_students * cafeteria_fraction

    # L2
    original_outside_students = total_students - original_cafeteria_students

    # L3
    ran_inside_fraction = Fraction(1, 3) # one-third of the students outside
    students_ran_inside = original_outside_students * ran_inside_fraction

    # L4
    students_went_outside = 3 # 3 of the students in the cafeteria went outside
    net_change_cafeteria = students_ran_inside - students_went_outside

    # L5
    final_cafeteria_students = original_cafeteria_students + net_change_cafeteria

    # FA
    answer = final_cafeteria_students
    return answer