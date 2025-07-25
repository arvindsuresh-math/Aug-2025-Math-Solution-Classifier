def solve():
    """Index: 4128.
    Returns: the total number of hours spent moving.
    """
    # L1
    filling_time_per_trip = 15 # 15 minutes filling the car
    driving_time_to_new_house_per_trip = 30 # 30 minutes driving from the previous house to the new house
    time_per_one_way_trip = filling_time_per_trip + driving_time_to_new_house_per_trip

    # L2
    num_trips = 6 # In total they make 6 trips
    total_one_way_trip_time = time_per_one_way_trip * num_trips

    # L3
    num_return_trips = 5 # 5 times to complete the move
    total_return_trip_time = driving_time_to_new_house_per_trip * num_return_trips

    # L4
    total_minutes_spent = total_one_way_trip_time + total_return_trip_time

    # L5
    minutes_per_hour = 60 # WK
    total_hours_spent = total_minutes_spent / minutes_per_hour

    # FA
    answer = total_hours_spent
    return answer