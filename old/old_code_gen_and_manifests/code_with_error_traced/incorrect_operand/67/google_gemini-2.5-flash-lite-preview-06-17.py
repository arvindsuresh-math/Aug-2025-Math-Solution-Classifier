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
    jesse_miles_first_3_days = 3 * jesse_avg_first_3_days # eval: 2.0 = 3 * 0.6666666666666666

    #: L2
    jesse_miles_remaining = total_miles - jesse_avg_first_3_days - jesse_miles_first_3_days # eval: 27.333333333333332 = 30 - 0.6666666666666666 - 2.0

    #: L3
    jesse_avg_last_3_days = jesse_miles_remaining / 3 # eval: 9.11111111111111 = 27.333333333333332 / 3

    #: L4
    mia_miles_first_4_days = 4 * mia_avg_first_4_days # eval: 12 = 4 * 3

    #: L5
    mia_miles_remaining = total_miles - mia_miles_first_4_days # eval: 18 = 30 - 12

    #: L6
    mia_avg_last_3_days = mia_miles_remaining / 3 # eval: 6.0 = 18 / 3

    #: L7
    total_avg_last_3_days = jesse_avg_last_3_days + mia_avg_last_3_days # eval: 15.11111111111111 = 9.11111111111111 + 6.0

    #: L8
    average_of_averages = total_avg_last_3_days / 2 # eval: 7.555555555555555 = 15.11111111111111 / 2

    #: FA
    answer = average_of_averages
    return answer # eval: return 7.555555555555555
