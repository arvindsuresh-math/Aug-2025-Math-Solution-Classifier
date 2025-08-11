from fractions import Fraction

def solve():
    """Index: 5558.
    Returns: the number of girls in the class.
    """
    # L1
    boys_ratio_part = 5 # The ratio of boys to girls in a math class is 5:8
    girls_ratio_part = 8 # The ratio of boys to girls in a math class is 5:8
    total_ratio_parts = boys_ratio_part + girls_ratio_part

    # L2
    total_students = 260 # total number of students in the class is 260
    boys_fraction = Fraction(boys_ratio_part, total_ratio_parts)
    num_boys = boys_fraction * total_students

    # L3
    num_girls = total_students - num_boys

    # FA
    answer = num_girls
    return answer