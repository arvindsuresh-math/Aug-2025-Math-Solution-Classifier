def solve():
    """Index: 1231.
    Returns: the difference in speed between the two spacecraft in miles per hour.
    """
    # L1
    first_spacecraft_flight_minutes = 30 # left New Orleans airport at 3:00 pm to travel the 448-mile distance to Dallas by air. Traveling nonstop, the first spacecraft landed in Dallas at 3:30 pm
    minutes_per_hour = 60 # WK
    first_spacecraft_flight_hours = first_spacecraft_flight_minutes / minutes_per_hour

    # L2
    additional_minutes_second_spacecraft = 30 # thirty minutes later
    second_spacecraft_flight_minutes = first_spacecraft_flight_minutes + additional_minutes_second_spacecraft
    second_spacecraft_flight_hours = second_spacecraft_flight_minutes / minutes_per_hour

    # L3
    distance_miles = 448 # 448-mile distance
    first_spacecraft_speed_mph = distance_miles / first_spacecraft_flight_hours

    # L4
    second_spacecraft_speed_mph = distance_miles / second_spacecraft_flight_hours

    # L5
    speed_difference_mph = first_spacecraft_speed_mph - second_spacecraft_speed_mph

    # FA
    answer = speed_difference_mph
    return answer