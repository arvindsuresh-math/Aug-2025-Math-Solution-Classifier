def solve():
    """Index: 6021.
    Returns: the total number of minutes Harry will have spent traveling.
    """
    # L1
    initial_bus_time = 15 # already been sat on the bus for 15 minutes
    remaining_bus_time = 25 # rest of the journey will take another 25 minutes
    total_bus_journey_time = initial_bus_time + remaining_bus_time

    # L2
    walk_time_divisor = 2 # half the amount of time
    walk_time = total_bus_journey_time / walk_time_divisor

    # L3
    total_travel_time = total_bus_journey_time + walk_time

    # FA
    answer = total_travel_time
    return answer