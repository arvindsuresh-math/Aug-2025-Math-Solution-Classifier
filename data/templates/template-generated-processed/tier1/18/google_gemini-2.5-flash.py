def solve():
    """Index: 18.
    Returns: the total hours Roque takes to get to and from work a week with walking and biking.
    """
    # L1
    walk_time_one_way = 2 # two hours to walk to work
    walk_trips_per_week = 3 # walks to and from work three times a week
    walk_hours_to_work_per_week = walk_time_one_way * walk_trips_per_week

    # L2
    trips_per_round_trip = 2 # WK
    total_walk_hours_per_week = walk_hours_to_work_per_week * trips_per_round_trip

    # L3
    bike_time_one_way = 1 # one hour to ride his bike to work
    bike_trips_per_week = 2 # rides his bike to and from work twice a week
    bike_hours_to_work_per_week = bike_time_one_way * bike_trips_per_week

    # L4
    total_bike_hours_per_week = bike_hours_to_work_per_week * trips_per_round_trip

    # L5
    total_hours_per_week = total_walk_hours_per_week + total_bike_hours_per_week

    # FA
    answer = total_hours_per_week
    return answer