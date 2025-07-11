def solve():
    """Index: 979.
    Returns: how much farther Kyle threw the ball compared to Parker.
    """
    # L1
    parker_distance = 16 # Parker threw the ball 16 yards
    grant_percent_farther = 0.25 # Grant threw the ball 25 percent farther
    grant_extra_distance = parker_distance * grant_percent_farther

    # L2
    grant_total_distance = parker_distance + grant_extra_distance

    # L3
    kyle_multiplier = 2 # Kyle threw the ball 2 times farther than Grant
    kyle_distance = kyle_multiplier * grant_total_distance

    # L4
    answer = kyle_distance - parker_distance
    return answer