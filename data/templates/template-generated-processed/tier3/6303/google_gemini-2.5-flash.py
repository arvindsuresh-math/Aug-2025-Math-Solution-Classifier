def solve():
    """Index: 6303.
    Returns: the number of red marbles Fred has.
    """
    # L1
    total_marbles = 63 # If he has 63 marbles
    dark_blue_denominator = 3 # At least a third of Fred's marbles
    dark_blue_marbles = total_marbles / dark_blue_denominator

    # L2
    red_and_green_marbles = total_marbles - dark_blue_marbles

    # L3
    green_marbles = 4 # except for 4 that are green
    red_marbles = red_and_green_marbles - green_marbles

    # FA
    answer = red_marbles
    return answer