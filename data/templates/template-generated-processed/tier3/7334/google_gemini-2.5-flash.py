def solve():
    """Index: 7334.
    Returns: the total number of marbles Alex has.
    """
    # L1
    alex_black_multiplier = 2 # twice as many black marbles as Lorin
    lorin_black_marbles = 4 # Lorin has 4 black marbles
    alex_black_marbles = alex_black_multiplier * lorin_black_marbles

    # L2
    jimmy_yellow_marbles = 22 # Jimmy has 22 yellow marbles
    alex_yellow_divisor = 2 # one half as many yellow marbles as Jimmy
    alex_yellow_marbles = jimmy_yellow_marbles / alex_yellow_divisor

    # L3
    total_alex_marbles = alex_black_marbles + alex_yellow_marbles

    # FA
    answer = total_alex_marbles
    return answer