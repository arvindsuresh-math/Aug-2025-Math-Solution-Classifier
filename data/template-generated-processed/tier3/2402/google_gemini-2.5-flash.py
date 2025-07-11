from fractions import Fraction

def solve():
    """Index: 2402.
    Returns: the number of students who did not participate in the competition.
    """
    # L1
    total_students = 39 # class of 39 students
    participated_fraction = Fraction(1, 3) # One-third of a class
    students_participated = total_students * participated_fraction

    # L2
    students_not_participated = total_students - students_participated

    # FA
    answer = students_not_participated
    return answer