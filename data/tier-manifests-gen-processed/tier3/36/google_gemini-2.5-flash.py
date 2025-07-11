def solve():
    """Index: 36.
    Returns: the difference in earnings between Lisa and Tommy.
    """
    # L1
    total_earnings = 60 # $60 from washing cars
    lisa_fraction_earned = 1/2 # half of the $60
    lisa_earnings = total_earnings * lisa_fraction_earned

    # L2
    tommy_fraction_earned = 1/2 # half of what Lisa earned
    tommy_earnings = lisa_earnings * tommy_fraction_earned

    # L3
    difference_lisa_tommy = lisa_earnings - tommy_earnings

    # FA
    answer = difference_lisa_tommy
    return answer