from fractions import Fraction

def solve():
    """Index: 1587.
    Returns: the total number of smoking students who have not been hospitalized.
    """
    # L1
    total_students = 300 # class of 300 students
    smoking_percentage = Fraction(40, 100) # 40% of the class
    smoking_students = smoking_percentage * total_students

    # L2
    hospitalized_percentage = Fraction(70, 100) # 70% of the smoking students are hospitalized
    hospitalized_students = hospitalized_percentage * smoking_students

    # L3
    non_hospitalized_smoking_students = smoking_students - hospitalized_students

    # FA
    answer = non_hospitalized_smoking_students
    return answer