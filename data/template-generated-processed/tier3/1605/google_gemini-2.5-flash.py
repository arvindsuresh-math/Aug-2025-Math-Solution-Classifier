from fractions import Fraction

def solve():
    """Index: 1605.
    Returns: the number of students walking home.
    """
    # L1
    total_students = 92 # 92 students altogether
    students_on_bus = 20 # Twenty of them ride the school bus home
    students_not_on_bus = total_students - students_on_bus

    # L2
    bike_fraction = Fraction(5, 8) # 5/8 of the remaining
    students_on_bike = bike_fraction * students_not_on_bus

    # L3
    students_walking_home = students_not_on_bus - students_on_bike

    # FA
    answer = students_walking_home
    return answer