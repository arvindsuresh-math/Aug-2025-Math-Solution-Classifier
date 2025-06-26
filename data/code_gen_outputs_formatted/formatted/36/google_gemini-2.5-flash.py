def solve(
        total_earnings: int = 60, # earned $60 from washing cars all week
        lisa_earnings_fraction: float = 1/2, # half of the $60 was earned by Lisa
        tommy_earnings_fraction_of_lisa: float = 1/2 # Tommy earned half of what Lisa earned
    ):
    """Index: 36.
    Returns: the difference in earnings between Lisa and Tommy.
    """

    #: L1
    lisa_earnings = total_earnings * lisa_earnings_fraction

    #: L2
    tommy_earnings = lisa_earnings * tommy_earnings_fraction_of_lisa

    #: L3
    difference_lisa_tommy = lisa_earnings - tommy_earnings

    answer = difference_lisa_tommy # FINAL ANSWER
    return answer