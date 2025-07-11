def solve():
    """Index: 36.
    Returns: the amount more money Lisa earned than Tommy.
    """
    # L1
    total_earnings = 60 # $60 from washing cars all week
    lisa_fraction = 1/2 # half of the $60 was earned by Lisa
    lisa_earnings = total_earnings * lisa_fraction

    # L2
    tommy_fraction = 1/2 # Tommy earned half of what Lisa earned
    tommy_earnings = lisa_earnings * tommy_fraction

    # L3
    difference = lisa_earnings - tommy_earnings

    # FA
    answer = difference
    return answer