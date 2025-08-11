from fractions import Fraction

def solve():
    """Index: 2833.
    Returns: the total number of students who prefer goldfish.
    """
    # L1
    feldstein_fraction = Fraction(2, 3) # 2/3rds of the students preferred goldfish
    students_per_class = 30 # each class has 30 students
    feldstein_goldfish_students = feldstein_fraction * students_per_class

    # L2
    johnson_fraction = Fraction(1, 6) # 1/6 of the students preferred goldfish
    johnson_goldfish_students = johnson_fraction * students_per_class

    # L3
    henderson_fraction = Fraction(1, 5) # 1/5 of the students prefer goldfish
    henderson_goldfish_students = henderson_fraction * students_per_class

    # L4
    total_goldfish_preferrers = feldstein_goldfish_students + johnson_goldfish_students + henderson_goldfish_students

    # FA
    answer = total_goldfish_preferrers
    return answer