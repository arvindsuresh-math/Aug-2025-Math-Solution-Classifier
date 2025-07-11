from fractions import Fraction

def solve():
    """Index: 25.
    Returns: the total number of tennis balls Ralph did not hit.
    """
    # L1
    first_batch_total_balls = 100 # first 100 balls
    not_hit_first_batch_fraction = Fraction(3, 5) # not able to hit 3/5 of them
    not_hit_first_batch_count = not_hit_first_batch_fraction * first_batch_total_balls

    # L2
    second_batch_total_balls = 75 # next 75 tennis balls
    not_hit_second_batch_fraction = Fraction(2, 3) # not able to hit 2/3 of them
    not_hit_second_batch_count = not_hit_second_batch_fraction * second_batch_total_balls

    # L3
    total_not_hit_balls = not_hit_first_batch_count + not_hit_second_batch_count

    # FA
    answer = total_not_hit_balls
    return answer