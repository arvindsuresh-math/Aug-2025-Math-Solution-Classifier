from fractions import Fraction

def solve():
    """Index: 4939.
    Returns: the number of senior students who did not get any scholarships.
    """
    # L1
    total_senior_students = 300 # 300 senior students
    full_merit_percentage = Fraction(5, 100) # Five percent
    full_merit_scholarship_students = total_senior_students * full_merit_percentage

    # L2
    half_merit_percentage = Fraction(10, 100) # ten percent
    half_merit_scholarship_students = total_senior_students * half_merit_percentage

    # L3
    total_scholarship_students = full_merit_scholarship_students + half_merit_scholarship_students

    # L4
    no_scholarship_students = total_senior_students - total_scholarship_students

    # FA
    answer = no_scholarship_students
    return answer