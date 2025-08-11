from fractions import Fraction

def solve():
    """Index: 2829.
    Returns: the total number of pages Rob read.
    """
    # L1
    planned_hours = 3 # three hours reading
    minutes_per_hour = 60 # WK
    total_planned_minutes = planned_hours * minutes_per_hour

    # L2
    fraction_numerator = 3 # three-quarters
    fraction_denominator = 4 # three-quarters
    reading_fraction = Fraction(fraction_numerator, fraction_denominator)
    actual_reading_minutes = reading_fraction * total_planned_minutes

    # L3
    minutes_per_page = 15 # reads a page every fifteen minutes
    total_pages_read = actual_reading_minutes / minutes_per_page

    # FA
    answer = total_pages_read
    return answer