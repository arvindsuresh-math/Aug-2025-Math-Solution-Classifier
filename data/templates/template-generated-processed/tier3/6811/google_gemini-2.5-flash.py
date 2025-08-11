def solve():
    """Index: 6811.
    Returns: the number of orange marbles in the jar.
    """
    # L1
    total_marbles = 24 # There are 24 marbles in a jar
    half_divisor = 2 # Half are blue
    blue_marbles = total_marbles / half_divisor

    # L2
    red_marbles = 6 # There are 6 red marbles
    blue_and_red_marbles = blue_marbles + red_marbles

    # L3
    orange_marbles = total_marbles - blue_and_red_marbles

    # FA
    answer = orange_marbles
    return answer