def solve():
    """Index: 4379.
    Returns: the total time in minutes Jeremy takes to get to his parents' house.
    """
    # L1
    total_distance = 600 # 600 miles to visit his parents
    avg_speed = 50 # 50 miles per hour
    minutes_per_hour = 60 # WK
    driving_hours = total_distance / avg_speed
    driving_minutes = driving_hours * minutes_per_hour

    # L2
    rest_stop_interval_hours = 2 # Every two hours of driving
    num_rest_stops = (driving_hours // rest_stop_interval_hours) - 1

    # L3
    rest_stop_duration_minutes = 15 # 15 minutes
    total_rest_stop_minutes = num_rest_stops * rest_stop_duration_minutes

    # L4
    miles_per_gallon = 18 # 18 miles per gallon of gas
    gallons_per_refill = 15 # used 15 gallons
    miles_per_refill_interval = miles_per_gallon * gallons_per_refill

    # L5
    num_refuels = total_distance // miles_per_refill_interval

    # L6
    refuel_duration_minutes = 10 # 10 minutes
    total_refuel_minutes = num_refuels * refuel_duration_minutes

    # L7
    total_trip_minutes = driving_minutes + total_rest_stop_minutes + total_refuel_minutes

    # FA
    answer = total_trip_minutes
    return answer