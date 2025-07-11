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
    first_batch_not_hit_fraction = 1 - first_batch_hit_fraction
    first_batch_not_hit_count = first_batch_not_hit_fraction * first_batch_count

    #: L2
    second_batch_not_hit_fraction = 1 - second_batch_hit_fraction
    second_batch_not_hit_count = second_batch_not_hit_fraction * second_batch_count

    #: L3
    total_not_hit = first_batch_not_hit_count + second_batch_not_hit_count

    answer = total_not_hit # FINAL ANSWER
    return answer