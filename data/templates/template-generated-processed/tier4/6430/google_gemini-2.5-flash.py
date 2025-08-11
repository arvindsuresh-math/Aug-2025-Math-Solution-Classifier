def solve():
    """Index: 6430.
    Returns: the average time in minutes Tony spends to get to the store.
    """
    # L1
    store_distance = 4 # The store is 4 miles away
    walking_speed = 2 # When he walks, he goes 2 MPH
    sunday_time_hours = store_distance / walking_speed

    # L2
    minutes_per_hour = 60 # WK
    sunday_time_minutes = sunday_time_hours * minutes_per_hour

    # L3
    running_speed = 10 # When he runs he goes 10 MPH
    weekday_time_hours = store_distance / running_speed

    # L4
    weekday_time_minutes = weekday_time_hours * minutes_per_hour

    # L5
    total_time_minutes = sunday_time_minutes + weekday_time_minutes + weekday_time_minutes

    # L6
    num_trips = 3 # Sunday, Tuesday, and Thursday
    average_time_minutes = total_time_minutes / num_trips

    # FA
    answer = average_time_minutes
    return answer