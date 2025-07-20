def solve():
    """Index: 6353.
    Returns: the total miles flown by all birds.
    """
    # L1
    eagle_speed = 15 # 15 miles per hour
    flight_duration = 2 # 2 hours straight
    eagle_distance = eagle_speed * flight_duration

    # L2
    falcon_speed = 46 # 46 miles per hour
    falcon_distance = falcon_speed * flight_duration

    # L3
    pelican_speed = 33 # 33 miles per hour
    pelican_distance = pelican_speed * flight_duration

    # L4
    hummingbird_speed = 30 # 30 miles per hour
    hummingbird_distance = hummingbird_speed * flight_duration

    # L5
    total_miles = eagle_distance + falcon_distance + pelican_distance + hummingbird_distance

    # FA
    answer = total_miles
    return answer