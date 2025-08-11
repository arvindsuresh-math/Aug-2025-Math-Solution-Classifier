from fractions import Fraction

def solve():
    """Index: 3292.
    Returns: the total number of students in the school.
    """
    # L2
    deaf_students = 180 # If the number of deaf students is 180
    fraction_multiplier_numerator = 1 # three times the size of blind student population
    fraction_multiplier_denominator = 3 # three times the size of blind student population
    blind_students = Fraction(fraction_multiplier_numerator, fraction_multiplier_denominator) * deaf_students

    # L3
    total_students = deaf_students + blind_students

    # FA
    answer = total_students
    return answer