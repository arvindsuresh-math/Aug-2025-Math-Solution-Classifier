def solve():
    """Index: 2856.
    Returns: the total time in hours for Mary's business trip process.
    """
    # L1
    uber_to_house_time = 10 # It takes 10 minutes for her Uber to get to her house
    airport_time_multiplier = 5 # 5 times longer to get to the airport
    uber_to_airport_time = uber_to_house_time * airport_time_multiplier

    # L2
    bag_check_time = 15 # It takes 15 minutes to check her bag
    security_time_multiplier = 3 # three times as long to get through security
    security_time = bag_check_time * security_time_multiplier

    # L3
    boarding_wait_time = 20 # wait for 20 minutes for her flight to start boarding
    takeoff_wait_multiplier = 2 # twice as long before the plane is ready to take off
    takeoff_wait_time = boarding_wait_time * takeoff_wait_multiplier

    # L4
    total_minutes = uber_to_house_time + uber_to_airport_time + bag_check_time + security_time + boarding_wait_time + takeoff_wait_time

    # L5
    minutes_per_hour = 60 # WK
    total_hours = total_minutes / minutes_per_hour

    # FA
    answer = total_hours
    return answer