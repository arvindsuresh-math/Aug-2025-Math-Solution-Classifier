def solve():
    """Index: 6022.
    Returns: the number of trips needed to move all coconuts.
    """
    # L1
    barbie_capacity = 4 # Barbie can carry 4 coconuts at a time
    bruno_capacity = 8 # Bruno can carry 8 coconuts at a time
    combined_capacity_per_trip = barbie_capacity + bruno_capacity

    # L2
    total_coconuts = 144 # a pile of 144 coconuts
    number_of_trips = total_coconuts / combined_capacity_per_trip

    # FA
    answer = number_of_trips
    return answer