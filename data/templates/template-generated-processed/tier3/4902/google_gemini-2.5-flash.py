from fractions import Fraction

def solve():
    """Index: 4902.
    Returns: the number of pens Sally took home.
    """
    # L1
    pens_per_student = 7 # gave 7 pens to each student
    num_students = 44 # class of 44 students
    pens_given_to_students = pens_per_student * num_students

    # L2
    initial_pens = 342 # Sally took 342 pens
    remaining_pens = initial_pens - pens_given_to_students

    # L3
    fraction_left_in_locker_numerator = 1 # half of the remainder
    fraction_left_in_locker_denominator = 2 # half of the remainder
    pens_in_locker = remaining_pens * Fraction(fraction_left_in_locker_numerator, fraction_left_in_locker_denominator)

    # L4
    pens_taken_home = remaining_pens - pens_in_locker

    # FA
    answer = pens_taken_home
    return answer