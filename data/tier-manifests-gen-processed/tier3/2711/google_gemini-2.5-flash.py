from fractions import Fraction

def solve():
    """Index: 2711.
    Returns: the total volume of air inhaled.
    """
    # L1
    minutes_per_hour = 60 # WK

    # L2
    hours_in_day = 24 # 24 hours
    total_minutes = minutes_per_hour * hours_in_day

    # L3
    breaths_per_minute = 17 # 17 breaths per minute
    air_per_breath = Fraction(5, 9) # 5/9 liter of air
    numerator_part = breaths_per_minute * air_per_breath.numerator * total_minutes
    denominator_part = air_per_breath.denominator
    total_volume_inhaled = breaths_per_minute * air_per_breath * total_minutes

    # FA
    answer = total_volume_inhaled
    return answer