def solve(
    total_miles: int = 30, # They have one week to run 30 miles.
    jesse_avg_first_3_days: float = 2/3, # On the first three days Jesse averages (2/3) of a mile.
    jesse_day_4_miles: int = 10, # On day four she runs 10 miles.
    mia_avg_first_4_days: int = 3, # Mia averages 3 miles a day over the first 4 days.
    days_in_race: int = 7 # a week long race
):
    """Index: 67.
    Returns: the average of their average that they have to run over the final three days.
    """

    #: L1
    jesse_miles_first_3_days = 3 * jesse_avg_first_3_days

    #: L2
    jesse_miles_remaining = total_miles - jesse_day_4_miles - jesse_miles_first_3_days

    #: L3
    jesse_avg_last_3_days = jesse_miles_remaining / 3

    #: L4
    mia_miles_first_4_days = 4 * mia_avg_first_4_days

    #: L5
    mia_miles_remaining = total_miles - mia_miles_first_4_days

    #: L6
    mia_avg_last_3_days = mia_miles_remaining / 3

    #: L7
    total_avg_last_3_days = jesse_avg_last_3_days + mia_avg_last_3_days

    #: L8
    average_of_averages = total_avg_last_3_days / 2

    #: FA
    answer = average_of_averages
    return answer