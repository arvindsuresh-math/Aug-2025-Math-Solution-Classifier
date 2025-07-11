def solve(
    total_distance: int = 30, # They have one week to run 30 miles
    jesse_initial_days: int = 3, # On the first three days
    jesse_initial_avg_distance: float = 2/3, # Jesse averages (2/3) of a mile
    jesse_day_four_distance: int = 10, # On day four she runs 10 miles
    mia_initial_avg_distance: int = 3, # Mia averages 3 miles a day
    mia_initial_days: int = 4, # over the first 4 days
    final_days: int = 3 # over the final three days
):
    """Index: 67.
    Returns: the average of their required average distances over the final three days.
    """

    #: L1
    jesse_distance_initial = jesse_initial_days * jesse_initial_avg_distance # eval: 2.0 = 3 * 0.6666666666666666

    #: L2
    jesse_remaining_distance = total_distance - jesse_day_four_distance - jesse_distance_initial # eval: 18.0 = 30 - 10 - 2.0

    #: L3
    jesse_avg_final_days = jesse_remaining_distance / final_days # eval: 6.0 = 18.0 / 3

    #: L4
    mia_distance_initial = mia_initial_days * mia_initial_avg_distance # eval: 12 = 4 * 3

    #: L5
    mia_remaining_distance = total_distance - mia_distance_initial # eval: 18 = 30 - 12

    #: L6
    mia_avg_final_days = mia_remaining_distance / final_days # eval: 6.0 = 18 / 3

    #: L7
    total_avg_final_days = jesse_avg_final_days + mia_avg_final_days # eval: 12.0 = 6.0 + 6.0

    #: L8
    average_of_their_averages = -4.0 # eval: -4.0 = -4.0

    #: FA
    answer = average_of_their_averages
    return answer # eval: return -4.0
