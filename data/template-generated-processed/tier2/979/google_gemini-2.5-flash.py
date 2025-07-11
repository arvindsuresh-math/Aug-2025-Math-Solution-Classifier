def solve():
    """Index: 979.
    Returns: how much farther Kyle threw the ball compared to Parker.
    """
    # L1
    parker_distance = 16 # Parker threw the ball 16 yards
    grant_percent_farther = 0.25 # 25 percent farther
    grant_additional_distance = parker_distance * grant_percent_farther

    # L2
    grant_total_distance = parker_distance + grant_additional_distance

    # L3
    kyle_multiplier = 2 # 2 times farther than Grant
    kyle_total_distance = kyle_multiplier * grant_total_distance

    # L4
    kyle_farther_than_parker = kyle_total_distance - parker_distance

    # FA
    answer = kyle_farther_than_parker
    return answer