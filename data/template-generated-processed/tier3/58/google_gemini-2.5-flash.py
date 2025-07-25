from fractions import Fraction

def solve():
    """Index: 58.
    Returns: the total amount of money those 60 students get in a day.
    """
    # L1
    total_students = 60 # If he surveyed 60 students
    fraction_students_6_dollars = Fraction(2, 3) # 2/3 of the students
    students_6_dollars = total_students * fraction_students_6_dollars

    # L2
    students_4_dollars = total_students - students_6_dollars

    # L3
    allowance_6_dollars = 6 # $6 allowance per day
    sum_allowance_6_dollars_group = students_6_dollars * allowance_6_dollars

    # L4
    allowance_4_dollars = 4 # $4 a day
    sum_allowance_4_dollars_group = students_4_dollars * allowance_4_dollars

    # L5
    total_daily_allowance = sum_allowance_6_dollars_group + sum_allowance_4_dollars_group

    # FA
    answer = total_daily_allowance
    return answer