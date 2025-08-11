from fractions import Fraction

def solve():
    """Index: 35.
    Returns: the number of students who got a final grade of B and above.
    """
    # L2
    total_students = 60 # he has 60 students in Grade 5
    percent_b_and_above_numerator = 60 # 100% - 40% = 60%
    percent_b_and_above_denominator = 100 # percent
    percent_b_and_above = Fraction(percent_b_and_above_numerator, percent_b_and_above_denominator)
    students_b_and_above = total_students * percent_b_and_above

    # FA
    answer = students_b_and_above
    return answer