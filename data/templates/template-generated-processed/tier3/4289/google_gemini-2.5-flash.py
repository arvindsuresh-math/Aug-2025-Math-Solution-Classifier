def solve():
    """Index: 4289.
    Returns: the distance from Layla's house to the high school in miles.
    """
    # L1
    total_mileage = 10 # total mileage was 10 miles
    track_mileage = 4 # rode four miles around the running track
    round_trip_to_school_mileage = total_mileage - track_mileage

    # L2
    legs_in_round_trip = 2 # Each leg of the round-trip journey
    distance_to_high_school = round_trip_to_school_mileage / legs_in_round_trip

    # FA
    answer = distance_to_high_school
    return answer