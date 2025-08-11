from fractions import Fraction

def solve():
    """Index: 4310.
    Returns: the number of students registered for the course.
    """
    # L1
    students_yesterday = 70 # 70 students in the class yesterday
    twice_yesterday_students = students_yesterday * 2

    # L2
    percentage_less = Fraction(10, 100) # Ten percent less
    fewer_students = percentage_less * twice_yesterday_students

    # L3
    students_today = twice_yesterday_students - fewer_students

    # L4
    absent_today = 30 # 30 students are absent today
    total_registered_students = students_today + absent_today

    # FA
    answer = total_registered_students
    return answer