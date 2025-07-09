def solve(
    initial_balls: int = 175, # He loads up the machine with 175 tennis balls to start with
    first_batch_size: int = 100, # Out of the first 100 balls
    fraction_hit_first_batch: float = 2/5, # he manages to hit 2/5 of them
    second_batch_size: int = 75, # Of the next 75 tennis balls
    fraction_hit_second_batch: float = 1/3 # he manages to hit 1/3 of them
):
    """Index: 25.
    Returns: the total number of tennis balls Ralph did not hit.
    """

    #: L1
    fraction_not_hit_first_batch = 1 - fraction_hit_first_batch # eval: 0.6 = 1 - 0.4
    not_hit_first_batch = fraction_not_hit_first_batch * first_batch_size # eval: 60.0 = 0.6 * 100

    #: L2
    fraction_not_hit_second_batch = 1 - fraction_hit_second_batch # eval: 0.6666666666666667 = 1 - 0.3333333333333333
    not_hit_second_batch = 60.00000000000001 # eval: 60.00000000000001 = 60.00000000000001

    #: L3
    total_not_hit = not_hit_first_batch + not_hit_second_batch # eval: 120.0 = 60.0 + 60.00000000000001

    #: FA
    answer = total_not_hit
    return answer # eval: return 120.0
