def solve():
    """Index: 5113.
    Returns: the total distance the birds covered in the trips.
    """
    # L1
    round_trip_multiplier = 2 # WK
    distance_to_materials = 200 # 200 miles from where they were building the nest
    distance_per_bird_per_round_trip = round_trip_multiplier * distance_to_materials

    # L2
    num_round_trips = 10 # 10 round trips
    total_distance_one_bird = distance_per_bird_per_round_trip * num_round_trips

    # L3
    num_birds = 2 # Two birds
    total_distance_both_birds = total_distance_one_bird + total_distance_one_bird

    # FA
    answer = total_distance_both_birds
    return answer