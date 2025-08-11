from fractions import Fraction

def solve():
    """Index: 67.
    Returns: the average of their average that they have to run over the final three days.
    """
    # L1
    days_first_period_jesse = 3 # On the first three days
    jesse_avg_first_period = Fraction(2, 3) # Jesse averages (2/3) of a mile
    jesse_miles_first_period = days_first_period_jesse * jesse_avg_first_period

    # L2
    total_race_distance = 30 # run 30 miles
    jesse_day4_miles = 10 # On day four she runs 10 miles
    jesse_miles_remaining = total_race_distance - jesse_day4_miles - jesse_miles_first_period

    # L3
    remaining_days = 3 # final three days
    jesse_avg_remaining_days = jesse_miles_remaining / remaining_days

    # L4
    mia_days_first_period = 4 # over the first 4 days
    mia_avg_first_period = 3 # Mia averages 3 miles a day
    mia_miles_first_period = mia_days_first_period * mia_avg_first_period

    # L5
    mia_miles_remaining = total_race_distance - mia_miles_first_period

    # L6
    mia_avg_remaining_days = mia_miles_remaining / remaining_days

    # L7
    total_avg_remaining_days = jesse_avg_remaining_days + mia_avg_remaining_days

    # L8
    number_of_people = 2 # average of their average
    final_average_per_day = total_avg_remaining_days / number_of_people

    # FA
    answer = final_average_per_day
    return answer