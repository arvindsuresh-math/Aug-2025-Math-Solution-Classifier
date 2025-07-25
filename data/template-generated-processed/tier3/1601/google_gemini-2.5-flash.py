from fractions import Fraction

def solve():
    """Index: 1601.
    Returns: the total number of students with average height.
    """
    # L1
    short_fraction = Fraction(2, 5) # 2/5 of the total number of students
    total_students = 400 # the class has 400 students
    num_short_students = short_fraction * total_students

    # L2
    num_tall_students = 90 # 90 tall students
    total_short_and_tall = num_short_students + num_tall_students

    # L3
    num_average_height_students = total_students - total_short_and_tall

    # FA
    answer = num_average_height_students
    return answer