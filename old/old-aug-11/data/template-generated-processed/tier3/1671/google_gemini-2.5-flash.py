def solve():
    """Index: 1671.
    Returns: the time it takes to get to the point where the river is 80 yards wide.
    """
    # L1
    destination_width = 80 # river is 80 yards wide
    starting_width = 50 # river that is 50 yards wide at one end
    width_difference = destination_width - starting_width

    # L2
    width_increase_per_distance = 2 # increases from this end uniformly by 2 yards every 10 meters
    distance_for_increase = 10 # increases from this end uniformly by 2 yards every 10 meters
    distance_to_cover = (width_difference / width_increase_per_distance) * distance_for_increase

    # L3
    travel_rate = 5 # row along the river at a rate of 5 m/s
    time_taken = distance_to_cover / travel_rate

    # FA
    answer = time_taken
    return answer