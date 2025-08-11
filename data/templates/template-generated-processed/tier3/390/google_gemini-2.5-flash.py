from fractions import Fraction

def solve():
    """Index: 390.
    Returns: the number of weeks Oscar needs to train before the marathon.
    """
    # L1
    target_distance = 20 # reaches a 20-mile run
    current_distance = 2 # he has already run 2 miles
    distance_to_increase = target_distance - current_distance

    # L2
    weekly_increase_fraction = Fraction(2, 3) # add 2/3 of a mile each week
    weeks_needed = distance_to_increase / weekly_increase_fraction

    # FA
    answer = weeks_needed
    return answer