def solve(
    total_miles: int = 30,  # they have one week to run 30 miles
    jesse_avg_first_three_days: float = 2/3,  # Jesse averages (2/3) of a mile on the first three days
    jesse_day_four_miles: int = 10,  # On day four she runs 10 miles
    mia_avg_first_four_days: int = 3,  # Mia averages 3 miles a day over the first 4 days
    total_days: int = 7  # the race lasts one week (7 days)
):
    """Index: 67.
    Returns: the average of Jesse's and Mia's average miles per day they have to run over the final three days.
    """

    #: L1
    jesse_miles_first_three_days = 3 * jesse_avg_first_three_days # eval: 2.0 = 3 * 0.6666666666666666

    #: L2
    jesse_miles_left = total_miles - jesse_day_four_miles - jesse_miles_first_three_days # eval: 18.0 = 30 - 10 - 2.0

    #: L3
    jesse_avg_last_three_days = jesse_miles_left / 3 # eval: 6.0 = 18.0 / 3

    #: L4
    mia_miles_first_four_days = 4 * mia_avg_first_four_days # eval: 12 = 4 * 3

    #: L5
    mia_miles_left = total_miles - mia_miles_first_four_days # eval: 18 = 30 - 12

    #: L6
    mia_avg_last_three_days = mia_miles_left / 3 # eval: 6.0 = 18 / 3

    #: L7
    total_avg_last_three_days = jesse_avg_last_three_days + mia_avg_last_three_days # eval: 12.0 = 6.0 + 6.0

    #: L8
    average_of_averages = total_avg_last_three_days / 2 # eval: 6.0 = 12.0 / 2

    #: FA
    answer = average_of_averages
    return answer # eval: return 6.0
