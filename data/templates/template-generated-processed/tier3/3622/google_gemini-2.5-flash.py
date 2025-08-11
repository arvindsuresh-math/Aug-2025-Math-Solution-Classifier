from fractions import Fraction

def solve():
    """Index: 3622.
    Returns: the number of more pencils Jeanine has than Clare.
    """
    # L1
    jeanine_initial_pencils = 18 # 18 pencils
    clare_divisor = 2 # half as many pencils
    clare_pencils = jeanine_initial_pencils / clare_divisor

    # L2
    given_fraction = Fraction(1, 3) # one third of his pencils
    pencils_given_to_abby = given_fraction * jeanine_initial_pencils

    # L3
    jeanine_pencils_left = jeanine_initial_pencils - pencils_given_to_abby

    # L4
    difference_pencils = jeanine_pencils_left - clare_pencils

    # FA
    answer = difference_pencils
    return answer