from fractions import Fraction

def solve():
    """Index: 3215.
    Returns: the volume of the balloon after 2 hours.
    """
    # L1
    increase_fraction = Fraction(2, 5) # two-fifths of its previous volume
    original_volume = 500 # original volume is 500cm³
    increase_first_hour = increase_fraction * original_volume

    # L2
    volume_after_first_hour = original_volume + increase_first_hour

    # L3
    increase_second_hour = increase_fraction * volume_after_first_hour

    # L4
    volume_after_second_hour = volume_after_first_hour + increase_second_hour

    # FA
    answer = volume_after_second_hour
    return answer