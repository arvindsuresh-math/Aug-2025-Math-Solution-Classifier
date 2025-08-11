def solve():
    """Index: 5144.
    Returns: the total distance of Johny's journey.
    """
    # L1
    south_distance = 40 # traveled South 40 miles
    east_more_than_south = 20 # 20 more miles than the distance he took to travel to the south
    east_distance = south_distance + east_more_than_south

    # L2
    south_east_total_distance = east_distance + south_distance

    # L3
    north_multiplier = 2 # twice the distance he had traveled to the East
    north_distance = north_multiplier * east_distance

    # L4
    total_journey_distance = south_east_total_distance + north_distance

    # FA
    answer = total_journey_distance
    return answer