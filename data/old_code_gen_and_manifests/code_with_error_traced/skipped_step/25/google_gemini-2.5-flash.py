def solve(
        initial_load: int = 175, # He loads up the machine with 175 tennis balls to start with
        first_set_balls: int = 100, # Out of the first 100 balls
        fraction_hit_first_set: float = 2/5, # he manages to hit 2/5 of them
        second_set_balls: int = 75, # Of the next 75 tennis balls
        fraction_hit_second_set: float = 1/3 # he manages to hit 1/3 of them
    ):
    """Index: 25.
    Returns: the total number of tennis balls Ralph did not hit.
    """

    #: L1
    fraction_not_hit_first_set = 1 - fraction_hit_first_set # eval: 0.6 = 1 - 0.4

    #: L2
    fraction_not_hit_second_set = 1 - fraction_hit_second_set # eval: 0.6666666666666667 = 1 - 0.3333333333333333
    balls_not_hit_second_set = fraction_not_hit_second_set * second_set_balls # eval: 50.00000000000001 = 0.6666666666666667 * 75

    #: L3
    total_balls_not_hit = fraction_hit_second_set + balls_not_hit_second_set # eval: 50.33333333333334 = 0.3333333333333333 + 50.00000000000001

    #: FA
    answer = total_balls_not_hit
    return answer # eval: return 50.33333333333334
