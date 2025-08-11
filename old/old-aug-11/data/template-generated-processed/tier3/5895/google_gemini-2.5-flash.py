from fractions import Fraction

def solve():
    """Index: 5895.
    Returns: the height James can jump.
    """
    # L1
    mark_jump_height = 6 # Mark can jump 6 inches
    lisa_multiplier = 2 # double the height as Mark
    lisa_jump_height = mark_jump_height * lisa_multiplier

    # L2
    jacob_multiplier = 2 # double the height of Lisa
    jacob_jump_height = lisa_jump_height * jacob_multiplier

    # L3
    james_fraction = Fraction(2, 3) # James jumps 2/3 as high Jacob
    james_jump_height = jacob_jump_height * james_fraction

    # FA
    answer = james_jump_height
    return answer