from fractions import Fraction

def solve():
    """Index: 1795.
    Returns: the total number of blue marbles collected by the friends together.
    """
    # L1
    mary_red_multiplier = 2 # Mary collected twice as many red marbles as Jenny
    jenny_red_marbles = 30 # Jenny collected 30 red marbles
    mary_red_marbles = mary_red_multiplier * jenny_red_marbles

    # L2
    anie_red_more = 20 # collected 20 more red marbles than Mary
    anie_red_marbles = mary_red_marbles + anie_red_more

    # L3
    total_red_marbles = mary_red_marbles + anie_red_marbles + jenny_red_marbles

    # L4
    jenny_blue_marbles = 25 # 25 blue marbles
    anie_blue_multiplier = 2 # twice the number of blue marbles Jenny collected
    anie_blue_marbles = anie_blue_multiplier * jenny_blue_marbles

    # L5
    mary_blue_fraction = Fraction(1, 2) # half the number of blue marbles collected by Anie
    mary_blue_marbles = mary_blue_fraction * anie_blue_marbles

    # L6
    total_blue_marbles = anie_blue_marbles + mary_blue_marbles + jenny_blue_marbles

    # FA
    answer = total_blue_marbles
    return answer