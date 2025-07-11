from fractions import Fraction

def solve():
    """Index: 259.
    Returns: the number of students in class C.
    """
    # L1
    class_a_percentage = Fraction(40, 100) # 40% of the students are in class A
    total_students = 80 # teaches 80 students
    students_in_class_a = class_a_percentage * total_students

    # L2
    fewer_students_class_b = 21 # class B has 21 students fewer than class A
    students_in_class_b = students_in_class_a - fewer_students_class_b

    # L3
    students_in_class_c = total_students - students_in_class_a - students_in_class_b

    # FA
    answer = students_in_class_c
    return answer