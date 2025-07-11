from fractions import Fraction

def solve():
    """Index: 1525.
    Returns: the number of boys in the Biology class.
    """
    # L1
    physics_class_students = 200 # The Physics class has 200 students
    biology_class_divisor = 2 # half as many students as the Physics class
    biology_class_students = physics_class_students / biology_class_divisor

    # L2
    boys_fraction = Fraction(1, 4) # three times as many girls as boys (implies 1 boy for every 3 girls, total 4 parts, so boys are 1/4)
    boys_in_biology_class = boys_fraction * biology_class_students

    # FA
    answer = boys_in_biology_class
    return answer