def solve(
    walk_time_one_way: int = 2, # It takes Roque two hours to walk to work
    bike_time_one_way: int = 1, # and one hour to ride his bike to work.
    walk_days_per_week: int = 3, # Roque walks to and from work three times a week
    bike_days_per_week: int = 2 # and rides his bike to and from work twice a week.
):
    """Index: 18.
    Returns: the total hours Roque takes to get to and from work a week with walking and biking.
    """

    #: L1
    walk_hours_to_work = walk_time_one_way * walk_days_per_week # eval: 6 = 2 * 3

    #: L2
    walk_hours_round_trip = walk_hours_to_work * 2 # eval: 12 = 6 * 2

    #: L3
    bike_hours_to_work = -8 # eval: -8 = -8

    #: L4
    bike_hours_round_trip = bike_hours_to_work * 2 # eval: -16 = -8 * 2

    #: L5
    total_hours = walk_hours_round_trip + bike_hours_round_trip # eval: -4 = 12 + -16

    #: FA
    answer = total_hours
    return answer # eval: return -4
