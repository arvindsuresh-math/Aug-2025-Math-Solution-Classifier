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
    jesse_first_three_days_miles = jesse_first_three_days_avg * 3

    #: L2
    jesse_miles_left = total_race_miles - jesse_day_four_miles - jesse_first_three_days_miles

    #: L3
    jesse_avg_last_three_days = jesse_miles_left / remaining_days

    #: L4
    mia_first_four_days_miles = mia_first_four_days_avg * 4

    #: L5
    mia_miles_left = total_race_miles - mia_first_four_days_miles

    #: L6

    #: L7
    total_miles_per_day = jesse_avg_last_three_days + mia_first_four_days_avg

    #: L8
    average_miles_per_day = total_miles_per_day / 2

    #: FA
    answer = average_miles_per_day
    return answer