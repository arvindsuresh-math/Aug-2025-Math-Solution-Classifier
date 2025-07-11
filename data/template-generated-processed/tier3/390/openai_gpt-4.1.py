from fractions import Fraction

def solve():
    """Index: 390.
    Returns: the number of weeks Oscar should start training before the marathon.
    """
    # L1
    goal_miles = 20 # until he reaches a 20-mile run
    current_miles = 2 # he has already run 2 miles
    miles_to_increase = goal_miles - current_miles

    # L2
    weekly_increase = Fraction(2, 3) # add 2/3 of a mile each week
    weeks_needed = miles_to_increase / weekly_increase

    # FA
    answer = weeks_needed
    return answer