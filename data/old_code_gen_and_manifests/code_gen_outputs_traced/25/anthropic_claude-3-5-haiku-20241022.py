def solve(
    total_tennis_balls: int = 175,  # Ralph loads up the machine with 175 tennis balls
    first_batch_balls: int = 100,  # Out of the first 100 balls
    first_batch_hit_fraction: float = 2/5,  # he manages to hit 2/5 of them
    next_batch_balls: int = 75,  # Of the next 75 tennis balls
    next_batch_hit_fraction: float = 1/3  # he manages to hit 1/3 of them
):
    """Index: 25.
    Returns: the total number of tennis balls Ralph did not hit."""

    #: L1
    first_batch_missed_balls = (1 - first_batch_hit_fraction) * first_batch_balls # eval: 60.0 = (1 - 0.4) * 100

    #: L2
    next_batch_missed_balls = (1 - next_batch_hit_fraction) * next_batch_balls # eval: 50.00000000000001 = (1 - 0.3333333333333333) * 75

    #: L3
    total_missed_balls = first_batch_missed_balls + next_batch_missed_balls # eval: 110.0 = 60.0 + 50.00000000000001

    #: FA
    answer = total_missed_balls
    return answer # eval: return 110.0
