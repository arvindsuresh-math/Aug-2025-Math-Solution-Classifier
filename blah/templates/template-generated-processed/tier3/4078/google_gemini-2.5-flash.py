from fractions import Fraction

def solve():
    """Index: 4078.
    Returns: the total number of students in the class now.
    """
    # L1
    initial_boys = 15 # 15 boys in a class
    percentage_greater = Fraction(20, 100) # 20% greater
    original_girls = initial_boys + percentage_greater * initial_boys

    # L2
    doubling_factor = 2 # the number of girls doubled
    new_girls = original_girls * doubling_factor

    # L3
    total_students_now = initial_boys + new_girls

    # FA
    answer = total_students_now
    return answer