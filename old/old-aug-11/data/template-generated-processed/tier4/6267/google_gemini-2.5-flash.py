from fractions import Fraction

def solve():
    """Index: 6267.
    Returns: the number of minutes Mia spent studying each day.
    """
    # L1
    tv_fraction = Fraction(1, 5) # 1/5 of her day watching TV
    total_day_fraction = Fraction(5, 5) # WK
    remaining_fraction = total_day_fraction - tv_fraction

    # L2
    hours_in_day = 24 # WK
    time_left_hours = hours_in_day * remaining_fraction

    # L3
    study_divisor = 4 # 1/4 of the time left on studying
    study_hours = time_left_hours / study_divisor

    # L4
    minutes_per_hour = 60 # WK
    study_minutes = study_hours * minutes_per_hour

    # FA
    answer = study_minutes
    return answer