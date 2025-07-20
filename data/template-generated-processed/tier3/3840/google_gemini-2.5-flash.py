def solve():
    """Index: 3840.
    Returns: the number of dark blue marbles Fred has.
    """
    # L1
    red_marbles = 38 # 38 red marbles
    half_divisor = 2 # half as many green ones
    green_marbles = red_marbles / half_divisor

    # L2
    total_marbles = 63 # 63 marbles
    dark_blue_marbles = total_marbles - red_marbles - green_marbles

    # FA
    answer = dark_blue_marbles
    return answer