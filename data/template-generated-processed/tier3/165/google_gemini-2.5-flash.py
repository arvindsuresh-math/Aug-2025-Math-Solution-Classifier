def solve():
    """Index: 165.
    Returns: the total time in hours for the entire tour.
    """
    # L1
    miles_to_destination = 55 # drive 55 miles to the destination
    extra_miles_return = 10 # 10 miles farther
    return_trip_miles = miles_to_destination + extra_miles_return

    # L2
    total_travel_miles = miles_to_destination + return_trip_miles

    # L3
    minutes_per_mile = 2 # drive 1 mile for 2 minutes
    total_travel_minutes = total_travel_miles * minutes_per_mile

    # L4
    minutes_per_hour = 60 # WK
    travel_hours = total_travel_minutes / minutes_per_hour

    # L5
    stay_duration_hours = 2 # stayed 2 hours at the destination
    total_tour_hours = travel_hours + stay_duration_hours

    # FA
    answer = total_tour_hours
    return answer