from fractions import Fraction

def solve():
    """Index: 6599.
    Returns: the number of potatoes Johnson has left in the sack.
    """
    # L1
    gina_potatoes = 69 # gives Gina 69 potatoes
    twice_multiplier = 2 # WK
    tom_potatoes = gina_potatoes * twice_multiplier

    # L2
    anne_fraction = Fraction(1, 3) # one-third of the amount of potatoes
    anne_potatoes = tom_potatoes * anne_fraction

    # L3
    total_given_out = gina_potatoes + tom_potatoes + anne_potatoes

    # L4
    initial_sack_potatoes = 300 # the sack contains 300 potatoes
    potatoes_left = initial_sack_potatoes - total_given_out

    # FA
    answer = potatoes_left
    return answer