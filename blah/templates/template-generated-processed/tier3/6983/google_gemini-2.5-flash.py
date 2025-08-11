def solve():
    """Index: 6983.
    Returns: the total number of people who will get to ride the Ferris wheel.
    """
    # L1
    end_time_hour = 7 # until 7:00 pm
    start_time_hour = 1 # from 1:00 pm
    open_hours = end_time_hour - start_time_hour

    # L2
    minutes_per_hour = 60 # WK
    ride_duration_minutes = 20 # 20 minutes
    rides_per_hour = minutes_per_hour / ride_duration_minutes

    # L3
    capacity_per_ride = 70 # 70 people
    people_per_hour = rides_per_hour * capacity_per_ride

    # L4
    total_people_can_ride = open_hours * people_per_hour

    # FA
    answer = total_people_can_ride
    return answer