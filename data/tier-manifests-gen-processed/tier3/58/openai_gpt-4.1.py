from fractions import Fraction

def solve():
    """Index: 58.
    Returns: the total daily allowance of the 60 students surveyed.
    """
    # L1
    total_students = 60 # he surveyed 60 students
    fraction_six_dollars = Fraction(2, 3) # 2/3 of the students receive an average of $6
    students_six_dollars = total_students * fraction_six_dollars

    # L2
    students_four_dollars = total_students - students_six_dollars

    # L3
    allowance_six = 6 # $6 allowance per day
    total_six_dollar_allowance = students_six_dollars * allowance_six

    # L4
    allowance_four = 4 # $4 a day
    total_four_dollar_allowance = students_four_dollars * allowance_four

    # L5
    total_allowance = total_six_dollar_allowance + total_four_dollar_allowance

    # FA
    answer = total_allowance
    return answer