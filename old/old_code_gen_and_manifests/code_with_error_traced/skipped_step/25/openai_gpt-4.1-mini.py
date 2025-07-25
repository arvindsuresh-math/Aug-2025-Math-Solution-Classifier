def solve(
    total_balls: int = 175,  # Ralph loads up the machine with 175 tennis balls
    first_batch: int = 100,  # Out of the first 100 balls
    hit_fraction_first: float = 2/5,  # he manages to hit 2/5 of them
    second_batch: int = 75,  # Of the next 75 tennis balls
    hit_fraction_second: float = 1/3  # he manages to hit 1/3 of them
):
    """Index: 25.
    Returns: the total number of tennis balls Ralph did not hit.
    """

    #: L1
    not_hit_first = (1 - hit_fraction_first) * first_batch # eval: 60.0 = (1 - 0.4) * 100

    #: L2
    not_hit_second = (1 - hit_fraction_second) * second_batch # eval: 50.00000000000001 = (1 - 0.3333333333333333) * 75

    #: L3

    #: FA
    answer = hit_fraction_second
    return answer # eval: return 0.3333333333333333
