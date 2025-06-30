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
    jesse_distance_initial = jesse_initial_days * jesse_initial_avg_distance

    #: L2
    jesse_remaining_distance = total_distance - jesse_day_four_distance - jesse_distance_initial

    #: L3
    jesse_avg_final_days = jesse_remaining_distance / final_days

    #: L4
    mia_distance_initial = mia_initial_days * mia_initial_avg_distance

    #: L5
    mia_remaining_distance = total_distance - mia_distance_initial

    #: L6
    mia_avg_final_days = mia_remaining_distance / final_days

    #: L7
    total_avg_final_days = total_distance + mia_avg_final_days

    #: L8
    average_of_their_averages = total_avg_final_days / 2

    #: FA
    answer = average_of_their_averages
    return answer