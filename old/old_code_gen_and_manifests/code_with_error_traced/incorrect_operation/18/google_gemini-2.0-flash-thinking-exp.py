def solve(
    walk_time_one_way: int = 2, # It takes Roque two hours to walk to work
    bike_time_one_way: int = 1, # and one hour to ride his bike to work
    walk_days_per_week: int = 3, # Roque walks to and from work three times a week
    bike_days_per_week: int = 2 # and rides his bike to and from work twice a week
):
    """Index: 18.
    Returns: the total hours Roque takes to get to and from work per week by walking and biking.
    """

    #: L1
    walk_time_to_work_per_week = walk_time_one_way * walk_days_per_week # eval: 6 = 2 * 3

    #: L2
    total_walk_time_per_week = walk_time_to_work_per_week * 2 # eval: 12 = 6 * 2

    #: L3
    bike_time_to_work_per_week = bike_time_one_way + bike_days_per_week # eval: 3 = 1 + 2

    #: L4
    total_bike_time_per_week = bike_time_to_work_per_week * 2 # eval: 6 = 3 * 2

    #: L5
    total_time_per_week = total_walk_time_per_week + total_bike_time_per_week # eval: 18 = 12 + 6

    #: FA
    answer = total_time_per_week
    return answer # eval: return 18
