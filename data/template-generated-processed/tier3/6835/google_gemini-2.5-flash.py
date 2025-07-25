def solve():
    """Index: 6835.
    Returns: the maximum number of times a person can ski down the mountain.
    """
    # L1
    lift_ride_time = 15 # 15 minutes to ride the lift
    ski_down_time = 5 # 5 minutes to ski back down
    time_per_trip = lift_ride_time + ski_down_time

    # L2
    total_hours = 2 # in 2 hours
    minutes_per_hour = 60 # WK
    total_minutes = total_hours * minutes_per_hour

    # L3
    number_of_trips = total_minutes / time_per_trip

    # FA
    answer = number_of_trips
    return answer