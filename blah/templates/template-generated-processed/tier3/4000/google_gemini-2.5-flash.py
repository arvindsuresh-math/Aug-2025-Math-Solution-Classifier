def solve():
    """Index: 4000.
    Returns: the difference in distance traveled between Mark's and Jenny's bottle caps.
    """
    # L1
    jenny_initial_distance = 18 # Jenny's bottlecap flies 18 feet straight
    jenny_bounce_denominator = 3 # 1/3 of the distance it already went
    jenny_bounce_distance = jenny_initial_distance / jenny_bounce_denominator

    # L2
    jenny_total_distance = jenny_bounce_distance + jenny_initial_distance

    # L3
    mark_initial_distance = 15 # Mark's bottle cap flies 15 feet forward
    mark_bounce_multiplier = 2 # flies twice as far as it already did
    mark_bounce_distance = mark_initial_distance * mark_bounce_multiplier

    # L4
    mark_total_distance = mark_bounce_distance + mark_initial_distance

    # L5
    distance_difference = mark_total_distance - jenny_total_distance

    # FA
    answer = distance_difference
    return answer