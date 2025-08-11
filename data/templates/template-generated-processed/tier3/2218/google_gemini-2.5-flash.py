def solve():
    """Index: 2218.
    Returns: the percentage difference in tail size.
    """
    # L1
    western_segments = 8 # Western rattlesnakes have 8 segments
    eastern_segments = 6 # Eastern rattlesnakes have 6 segments
    difference_in_segments = western_segments - eastern_segments

    # L2
    percentage_multiplier = 100 # multiply by 100%
    percentage_difference = (difference_in_segments / western_segments) * percentage_multiplier

    # FA
    answer = percentage_difference
    return answer