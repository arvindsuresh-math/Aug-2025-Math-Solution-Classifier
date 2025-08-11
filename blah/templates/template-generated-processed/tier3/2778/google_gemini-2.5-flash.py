from fractions import Fraction

def solve():
    """Index: 2778.
    Returns: the total number of complete laps Lexi must run.
    """
    # L1
    total_miles_whole = 3 # three and one-fourth miles
    lap_length_as_fraction = Fraction(1, 4) # a quarter of a mile
    one_fourth_miles_in_whole = total_miles_whole / lap_length_as_fraction

    # L2
    additional_lap_from_quarter_mile = 1 # one-fourth miles in three and one-fourth miles
    total_laps = one_fourth_miles_in_whole + additional_lap_from_quarter_mile

    # FA
    answer = total_laps
    return answer