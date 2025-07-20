def solve():
    """Index: 6619.
    Returns: the total driving time in hours.
    """
    # L1
    total_cattle = 400 # 400 head of cattle
    truck_capacity = 20 # 20 head of cattle
    num_trips = total_cattle / truck_capacity

    # L2
    travel_speed = 60 # 60 miles per hour
    distance = 60 # 60 miles
    one_way_time = distance / travel_speed

    # L3
    round_trip_factor = 2 # each trip requires driving to and returning
    round_trip_time = round_trip_factor * one_way_time

    # L4
    total_driving_time = num_trips * round_trip_time

    # FA
    answer = total_driving_time
    return answer