def solve():
    """Index: 1546.
    Returns: the number of minutes faster it is to take the airplane.
    """
    # L1
    driving_hours = 3 # 3 hours
    driving_minutes_extra = 15 # 15 minutes
    minutes_per_hour = 60 # WK
    total_driving_minutes = driving_hours * minutes_per_hour + driving_minutes_extra

    # L2
    airplane_fraction_denominator = 3 # one-third of the time
    airplane_flight_time = total_driving_minutes / airplane_fraction_denominator

    # L3
    drive_to_airport_time = 10 # drive 10 minutes to the airport
    wait_to_board_time = 20 # wait 20 minutes to board the plane
    get_off_plane_time = 10 # additional 10 minutes to get off the airplane
    total_airplane_trip_minutes = drive_to_airport_time + wait_to_board_time + airplane_flight_time + get_off_plane_time

    # L4
    minutes_faster = total_driving_minutes - total_airplane_trip_minutes

    # FA
    answer = minutes_faster
    return answer