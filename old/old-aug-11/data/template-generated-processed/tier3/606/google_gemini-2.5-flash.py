from fractions import Fraction

def solve():
    """Index: 606.
    Returns: the number of marbles of a different color.
    """
    # L1
    red_marbles = 20 # 20 red marbles
    green_multiplier = 3 # three times more green marbles
    green_marbles = green_multiplier * red_marbles

    # L2
    yellow_percentage = Fraction(20, 100) # 20% of the green marbles
    yellow_marbles = green_marbles * yellow_percentage

    # L3
    total_marbles_multiplier = 3 # total of all marbles in the box is three times more than the number of green marbles
    total_marbles = total_marbles_multiplier * green_marbles

    # L4
    other_color_marbles = total_marbles - red_marbles - green_marbles - yellow_marbles

    # FA
    answer = other_color_marbles
    return answer