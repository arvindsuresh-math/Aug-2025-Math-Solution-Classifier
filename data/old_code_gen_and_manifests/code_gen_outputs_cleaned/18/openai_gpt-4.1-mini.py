def solve(
    walk_time_one_way: int = 2,  # two hours to walk to work
    bike_time_one_way: int = 1,  # one hour to ride bike to work
    walk_trips_per_week: int = 3,  # walks to and from work three times a week
    bike_trips_per_week: int = 2   # rides bike to and from work twice a week
):
    """Index: 18.
    Returns: the total hours Roque spends walking and biking to and from work in a week.
    """
    #: L1
    walk_time_to_work_week = walk_time_one_way * walk_trips_per_week

    #: L2
    walk_time_total_week = walk_time_to_work_week * 2

    #: L3
    bike_time_to_work_week = bike_time_one_way * bike_trips_per_week

    #: L4
    bike_time_total_week = bike_time_to_work_week * 2

    #: L5
    total_time_week = walk_time_total_week + bike_time_total_week

    answer = total_time_week  # FINAL ANSWER
    return answer