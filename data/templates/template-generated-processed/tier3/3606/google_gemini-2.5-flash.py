from fractions import Fraction

def solve():
    """Index: 3606.
    Returns: the total number of middle schoolers.
    """
    # L1
    total_students = 800 # In a school with 800 students
    girls_fraction = Fraction(5, 8) # 5/8 of the students are girls
    num_girls = total_students * girls_fraction

    # L2
    num_boys = total_students - num_girls

    # L3
    girls_primary_fraction = Fraction(7, 10) # Seven-tenths of the girls
    girls_primary_grades = num_girls * girls_primary_fraction

    # L4
    girls_middle_school = num_girls - girls_primary_grades

    # L5
    boys_primary_fraction = Fraction(2, 5) # two-fifths of the boys
    boys_primary_grades = num_boys * boys_primary_fraction

    # L6
    boys_middle_school = num_boys - boys_primary_grades

    # L7
    total_middle_schoolers = girls_middle_school + boys_middle_school

    # FA
    answer = total_middle_schoolers
    return answer