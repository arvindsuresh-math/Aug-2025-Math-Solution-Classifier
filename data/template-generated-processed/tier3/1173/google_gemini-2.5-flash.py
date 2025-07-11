from fractions import Fraction

def solve():
    """Index: 1173.
    Returns: the amount of time Audrey was not dreaming.
    """
    # L1
    total_sleep_hours = 10 # asleep for 10 hours last night
    dream_fraction = Fraction(2, 5) # dreamed for 2/5 of the time
    dream_hours = dream_fraction * total_sleep_hours

    # L2
    non_dream_hours = total_sleep_hours - dream_hours

    # FA
    answer = non_dream_hours
    return answer