from fractions import Fraction

def solve():
    """Index: 67.
    Returns: the average of Jesse and Mia's required daily average over the final three days.
    """
    # L1
    jesse_days_first = 3 # first three days
    jesse_avg_first = Fraction(2, 3) # Jesse averages (2/3) of a mile
    jesse_miles_first = jesse_days_first * jesse_avg_first

    # L2
    total_miles = 30 # one week to run 30 miles
    jesse_day4 = 10 # day four she runs 10 miles
    jesse_miles_left = total_miles - jesse_day4 - jesse_miles_first

    # L3
    days_left = 3 # final three days
    jesse_avg_final = jesse_miles_left / days_left

    # L4
    mia_days_first = 4 # first 4 days
    mia_avg_first = 3 # Mia averages 3 miles a day
    mia_miles_first = mia_days_first * mia_avg_first

    # L5
    mia_miles_left = total_miles - mia_miles_first

    # L6
    mia_avg_final = mia_miles_left / days_left

    # L7
    total_avg_final = jesse_avg_final + mia_avg_final

    # L8
    num_runners = 2 # both Jesse and Mia
    answer = total_avg_final / num_runners
    return answer