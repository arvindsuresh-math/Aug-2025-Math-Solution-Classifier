from fractions import Fraction

def solve():
    """Index: 2199.
    Returns: the total number of foreign students at the University.
    """
    # L1
    foreign_percentage = Fraction(30, 100) # 30% of all the students
    total_students = 1800 # 1800 students
    initial_foreign_students = foreign_percentage * total_students

    # L2
    new_foreign_students = 200 # 200 new foreign students
    total_foreign_students = initial_foreign_students + new_foreign_students

    # FA
    answer = total_foreign_students
    return answer