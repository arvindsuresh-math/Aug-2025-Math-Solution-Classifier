def solve():
    """Index: 5349.
    Returns: the remaining distance to the hotel.
    """
    # L1
    initial_speed = 50 # 50 miles/hour
    initial_time = 3 # 3 hours straight
    initial_distance = initial_speed * initial_time

    # L2
    second_speed = 80 # 80 miles/hour
    second_time = 4 # 4 hours
    second_distance = second_speed * second_time

    # L3
    total_distance_traveled = initial_distance + second_distance

    # L4
    total_trip_distance = 600 # travel 600 miles to the hotel
    remaining_distance = total_trip_distance - total_distance_traveled

    # FA
    answer = remaining_distance
    return answer