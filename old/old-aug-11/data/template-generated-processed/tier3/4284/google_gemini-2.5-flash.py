from fractions import Fraction

def solve():
    """Index: 4284.
    Returns: the total number of pencils remaining altogether.
    """
    # L1
    jeff_initial_pencils = 300 # Jeff had 300 pencils
    jeff_donated_percentage = Fraction(30, 100) # donated 30% of them
    jeff_donated_pencils = jeff_donated_percentage * jeff_initial_pencils

    # L2
    jeff_remaining_pencils = jeff_initial_pencils - jeff_donated_pencils

    # L3
    vicki_multiplier = 2 # twice as many pencils as Jeff
    vicki_initial_pencils = vicki_multiplier * jeff_initial_pencils

    # L4
    vicki_donated_fraction = Fraction(3, 4) # donated 3/4 of his pencils
    vicki_donated_pencils = vicki_donated_fraction * vicki_initial_pencils

    # L5
    vicki_remaining_pencils = vicki_initial_pencils - vicki_donated_pencils

    # L6
    total_remaining_pencils = vicki_remaining_pencils + jeff_remaining_pencils

    # FA
    answer = total_remaining_pencils
    return answer