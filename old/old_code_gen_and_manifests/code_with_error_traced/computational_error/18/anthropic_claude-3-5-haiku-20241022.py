def solve(
        walking_time_one_way: int = 2,  # It takes Roque two hours to walk to work
        biking_time_one_way: int = 1,   # one hour to ride his bike to work
        walking_days_per_week: int = 3, # walks to and from work three times a week
        biking_days_per_week: int = 2   # rides his bike to and from work twice a week
    ):
    """Index: 18.
    Returns: the total hours Roque spends commuting to and from work in a week.
    """

    #: L1
    walking_time_to_work = walking_time_one_way * walking_days_per_week # eval: 6 = 2 * 3

    #: L2
    walking_time_round_trip = walking_time_to_work * 2 # eval: 12 = 6 * 2

    #: L3
    biking_time_to_work = -8 # eval: -8 = -8

    #: L4
    biking_time_round_trip = biking_time_to_work * 2 # eval: -16 = -8 * 2

    #: L5
    total_commute_time = walking_time_round_trip + biking_time_round_trip # eval: -4 = 12 + -16

    #: FA
    answer = total_commute_time
    return answer # eval: return -4
