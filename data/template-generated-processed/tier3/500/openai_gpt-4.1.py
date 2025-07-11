def solve():
    """Index: 500.
    Returns: the number of times Tammy caught the ball.
    """
    # L1
    joe_catches = 23 # Joe caught the ball 23 times
    derek_multiplier = 2 # double the catches Joe did
    derek_subtract = 4 # four less than double
    derek_catches = derek_multiplier * joe_catches - derek_subtract

    # L2
    tammy_divisor = 3 # a third of the times Derek did
    tammy_add = 16 # sixteen more than a third
    tammy_catches = derek_catches / tammy_divisor + tammy_add

    # FA
    answer = tammy_catches
    return answer