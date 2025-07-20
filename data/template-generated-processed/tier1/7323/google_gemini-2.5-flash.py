def solve():
    """Index: 7323.
    Returns: the latest time they can leave their house.
    """
    # L1
    drive_time_minutes = 45 # 45 minutes to drive to the airport
    park_time_minutes = 15 # 15 minutes to park their vehicle
    total_travel_minutes = drive_time_minutes + park_time_minutes

    # L2
    total_travel_hours = 1 # (1 hour) derived from 60 minutes in L1
    recommended_check_in_hours = 2 # check in 2 hours early
    total_time_needed_hours = recommended_check_in_hours + total_travel_hours

    # L3
    flight_departure_hour = 8 # flight leaves at 8:00 pm
    latest_departure_hour = flight_departure_hour - total_time_needed_hours

    # FA
    answer = latest_departure_hour
    return answer