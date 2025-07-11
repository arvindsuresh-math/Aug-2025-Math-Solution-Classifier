def solve():
    """Index: 834.
    Returns: the number of green marbles Eric has.
    """
    # L1
    white_marbles = 12 # 12 white marbles
    blue_marbles = 6 # 6 blue marbles
    white_and_blue = white_marbles + blue_marbles

    # L2
    total_marbles = 20 # Eric has 20 marbles
    green_marbles = total_marbles - white_and_blue

    # FA
    answer = green_marbles
    return answer