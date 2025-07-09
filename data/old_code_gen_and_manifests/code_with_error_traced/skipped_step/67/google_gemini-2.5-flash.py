def solve(
        total_race_miles: int = 30, # They have one week to run 30 miles
        jesse_avg_first_three_days: float = 2/3, # On the first three days Jesse averages (2/3) of a mile
        jesse_day_four_miles: int = 10, # On day four she runs 10 miles
        mia_avg_first_four_days: int = 3, # Mia averages 3 miles a day over the first 4 days
        num_first_three_days: int = 3, # On the first three days
        num_first_four_days: int = 4, # over the first 4 days
        num_final_days: int = 3 # over the final three days
    ):
    """Index: 67.
    Returns: the average of their average daily miles that they have to run over the final three days.
    """

    #: L1
    jesse_miles_first_three_days = num_first_three_days * jesse_avg_first_three_days # eval: 2.0 = 3 * 0.6666666666666666

    #: L2
    jesse_remaining_miles = total_race_miles - jesse_day_four_miles - jesse_miles_first_three_days # eval: 18.0 = 30 - 10 - 2.0

    #: L3
    jesse_avg_final_three_days = jesse_remaining_miles / num_final_days # eval: 6.0 = 18.0 / 3

    #: L4
    mia_miles_first_four_days = num_first_four_days * mia_avg_first_four_days # eval: 12 = 4 * 3

    #: L5
    mia_remaining_miles = total_race_miles - mia_miles_first_four_days # eval: 18 = 30 - 12

    #: L6
    mia_avg_final_three_days = mia_remaining_miles / num_final_days # eval: 6.0 = 18 / 3

    #: L7
    total_avg_both = jesse_avg_final_three_days + mia_avg_final_three_days # eval: 12.0 = 6.0 + 6.0

    #: L8

    #: FA
    answer = num_first_three_days
    return answer # eval: return 3
