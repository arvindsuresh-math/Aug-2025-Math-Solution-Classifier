def solve():
    """Index: 500.
    Returns: the number of times Tammy caught the ball.
    """
    # L1
    joe_catches = 23 # He caught the ball 23 times
    double_factor = 2 # double the catches Joe did
    less_than_double = 4 # four less than double
    double_joe_catches = double_factor * joe_catches
    derek_catches = double_joe_catches - less_than_double

    # L2
    third_divisor = 3 # a third of the times Derek did
    more_than_third = 16 # sixteen more than a third
    third_of_derek_catches = derek_catches / third_divisor
    tammy_catches = third_of_derek_catches + more_than_third

    # FA
    answer = tammy_catches
    return answer