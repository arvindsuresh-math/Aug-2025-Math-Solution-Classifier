from fractions import Fraction

def solve():
    """Index: 7363.
    Returns: the total number of students who are not reading.
    """
    # L1
    total_girls = 12 # 12 girls
    reading_girls_fraction = Fraction(5, 6) # 5/6 of the girls
    reading_girls = total_girls * reading_girls_fraction

    # L2
    non_reading_girls = total_girls - reading_girls

    # L3
    total_boys = 10 # 10 boys
    reading_boys_fraction = Fraction(4, 5) # 4/5 of the boys
    reading_boys = total_boys * reading_boys_fraction

    # L4
    non_reading_boys = total_boys - reading_boys

    # L5
    total_non_reading_students = non_reading_girls + non_reading_boys

    # FA
    answer = total_non_reading_students
    return answer