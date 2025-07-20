from fractions import Fraction

def solve():
    """Index: 4034.
    Returns: the number of students who failed the exam.
    """
    # L1
    total_students = 80 # 80 students who took the biology exam
    fraction_100_percent = Fraction(2, 5) # only 2/5 of them managed to score 100%
    students_100_percent = fraction_100_percent * total_students

    # L2
    students_not_100_percent = total_students - students_100_percent

    # L3
    percentage_over_80 = Fraction(50, 100) # 50 percent of the remaining students
    students_over_80_percent = percentage_over_80 * students_not_100_percent

    # L4
    failed_students = students_not_100_percent - students_over_80_percent

    # FA
    answer = failed_students
    return answer