from fractions import Fraction

def solve():
    """Index: 259.
    Returns: the number of students in class C.
    """
    # L1
    percent_in_class_a = Fraction(40, 100) # 40% of the students are in class A
    total_students = 80 # 80 students
    class_a_students = percent_in_class_a * total_students

    # L2
    class_b_difference = 21 # class B has 21 students fewer than class A
    class_b_students = class_a_students - class_b_difference

    # L3
    class_c_students = total_students - class_a_students - class_b_students

    # FA
    answer = class_c_students
    return answer