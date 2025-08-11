from fractions import Fraction

def solve():
    """Index: 35.
    Returns: the number of students who got a final grade of B and above.
    """
    # L1
    total_percentage = 100 # WK
    below_b_percentage = 40 # 40% of his Grade 5 students got a final grade below B
    above_b_percentage = total_percentage - below_b_percentage

    # L2
    total_students = 60 # he has 60 students in Grade 5
    percentage_denominator = 100 # WK
    students_above_b = total_students * Fraction(above_b_percentage, percentage_denominator)

    # FA
    answer = students_above_b
    return answer