def solve(
    total_race_miles: int = 30,  # They have one week to run 30 miles
    jesse_first_three_days_avg: float = 2/3,  # On the first three days Jesse averages (2/3) of a mile
    jesse_day_four_miles: int = 10,  # On day four she runs 10 miles
    mia_first_four_days_avg: int = 3,  # Mia averages 3 miles a day over the first 4 days
    remaining_days: int = 3  # Final three days
):
    """Index: 67.
    Returns: the average miles per day they both need to run in the final three days."""

    #: L1
    jesse_first_three_days_miles = jesse_first_three_days_avg + 3 # eval: 3.6666666666666665 = 0.6666666666666666 + 3

    #: L2
    jesse_miles_left = total_race_miles - jesse_day_four_miles - jesse_first_three_days_miles # eval: 16.333333333333332 = 30 - 10 - 3.6666666666666665

    #: L3
    jesse_avg_last_three_days = jesse_miles_left / remaining_days # eval: 5.444444444444444 = 16.333333333333332 / 3

    #: L4
    mia_first_four_days_miles = mia_first_four_days_avg * 4 # eval: 12 = 3 * 4

    #: L5
    mia_miles_left = total_race_miles - mia_first_four_days_miles # eval: 18 = 30 - 12

    #: L6
    mia_avg_last_three_days = mia_miles_left / remaining_days # eval: 6.0 = 18 / 3

    #: L7
    total_miles_per_day = jesse_avg_last_three_days + mia_avg_last_three_days # eval: 11.444444444444443 = 5.444444444444444 + 6.0

    #: L8
    average_miles_per_day = total_miles_per_day / 2 # eval: 5.722222222222221 = 11.444444444444443 / 2

    #: FA
    answer = average_miles_per_day
    return answer # eval: return 5.722222222222221
