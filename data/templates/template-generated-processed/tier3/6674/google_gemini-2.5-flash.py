def solve():
    """Index: 6674.
    Returns: the total number of hours William spent on the road.
    """
    # L1
    arrival_time_24hr = 20 # arrived at his hometown by 8:00 PM
    departure_time_24hr = 7 # left Missouri by 7:00 AM
    total_journey_hours = arrival_time_24hr - departure_time_24hr

    # L2
    stop1_minutes = 25 # 3 stops of 25
    stop2_minutes = 10 # 10
    stop3_minutes = 25 # and 25 minutes respectively
    total_stop_minutes = stop1_minutes + stop2_minutes + stop3_minutes

    # L3
    minutes_per_hour = 60 # 60 minutes in an hour
    total_stop_hours = total_stop_minutes / minutes_per_hour

    # L4
    hours_on_road = total_journey_hours - total_stop_hours

    # FA
    answer = hours_on_road
    return answer