from fractions import Fraction

def solve():
    """Index: 2999.
    Returns: the number of red marbles.
    """
    # L1
    total_marbles = 50 # George collected 50 marbles
    half_divisor = 2 # Half of them are white
    white_marbles = total_marbles / half_divisor

    # L2
    green_percentage = Fraction(50, 100) # 50% fewer green balls
    yellow_marbles = 12 # 12 are yellow
    green_marbles = green_percentage * yellow_marbles

    # L3
    known_marbles_sum = white_marbles + yellow_marbles + green_marbles

    # L4
    red_marbles = total_marbles - known_marbles_sum

    # FA
    answer = red_marbles
    return answer