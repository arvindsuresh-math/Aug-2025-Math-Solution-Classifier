def solve(
    initial_balls: int = 175, # Ralph loads up the machine with 175 tennis balls to start with
    first_batch_count: int = 100, # Out of the first 100 balls
    first_batch_hit_fraction: float = 2/5, # he manages to hit 2/5 of them
    second_batch_count: int = 75, # Of the next 75 tennis balls
    second_batch_hit_fraction: float = 1/3 # he manages to hit 1/3 of them
):
    """Index: 25.
    Returns: the total number of tennis balls Ralph did not hit.
    """

    #: L1
    first_batch_not_hit_count = second_batch_count * first_batch_count # eval: 7500 = 75 * 100

    #: L2
    second_batch_not_hit_fraction = 1 - second_batch_hit_fraction # eval: 0.6666666666666667 = 1 - 0.3333333333333333
    second_batch_not_hit_count = second_batch_not_hit_fraction * second_batch_count # eval: 50.00000000000001 = 0.6666666666666667 * 75

    #: L3
    total_not_hit = first_batch_not_hit_count + second_batch_not_hit_count # eval: 7550.0 = 7500 + 50.00000000000001

    #: FA
    answer = total_not_hit
    return answer # eval: return 7550.0
