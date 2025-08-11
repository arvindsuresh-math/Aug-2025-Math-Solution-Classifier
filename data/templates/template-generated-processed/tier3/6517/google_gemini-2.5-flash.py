from fractions import Fraction

def solve():
    """Index: 6517.
    Returns: the total number of steps Mabel will walk to visit Helen.
    """
    # L1
    helen_fraction = Fraction(3, 4) # 3/4 the number of steps
    mabel_steps_east = 4500 # Mabel lives 4500 steps directly east
    helen_steps_west = helen_fraction * mabel_steps_east

    # L2
    total_steps = mabel_steps_east + helen_steps_west

    # FA
    answer = total_steps
    return answer