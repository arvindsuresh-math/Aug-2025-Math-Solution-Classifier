def solve():
    """Index: 3614.
    Returns: the total distance Robin walks.
    """
    # L1
    initial_walk_distance = 200 # walks 200 meters
    round_trip_to_house = initial_walk_distance + initial_walk_distance

    # L2
    distance_to_city_center = 500 # distance between Robin's house and the city center is 500 meters
    total_distance_walked = round_trip_to_house + distance_to_city_center

    # FA
    answer = total_distance_walked
    return answer