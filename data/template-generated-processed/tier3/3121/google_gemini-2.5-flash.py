from fractions import Fraction

def solve():
    """Index: 3121.
    Returns: the number of pizza slices left.
    """
    # L1
    slices_per_person = Fraction(3, 2) # 3/2 slices each
    number_of_people = 2 # Angeli and Marlon ate ... each
    total_slices_eaten = slices_per_person * number_of_people

    # L2
    initial_slices = 8 # A whole pizza was cut into 8 slices
    slices_left = initial_slices - total_slices_eaten

    # FA
    answer = slices_left
    return answer