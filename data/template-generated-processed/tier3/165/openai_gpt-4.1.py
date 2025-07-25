def solve():
    """Index: 165.
    Returns: the total time in hours for the entire tour.
    """
    # L1
    destination_miles = 55 # 55 miles to the destination
    return_extra_miles = 10 # 10 miles farther on the way back
    return_trip_miles = destination_miles + return_extra_miles

    # L2
    total_miles = destination_miles + return_trip_miles

    # L3
    minutes_per_mile = 2 # 1 mile for 2 minutes
    total_travel_minutes = total_miles * minutes_per_mile

    # L4
    minutes_per_hour = 60 # WK
    total_travel_hours = total_travel_minutes / minutes_per_hour

    # L5
    stay_hours = 2 # stayed 2 hours at the destination
    total_tour_hours = total_travel_hours + stay_hours

    # FA
    answer = total_tour_hours
    return answer