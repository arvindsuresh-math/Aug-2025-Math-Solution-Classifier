def solve(
    total_earned: int = 60, # Lisa, Jack, and Tommy earned $60
    lisa_fraction: float = 1/2, # half of the $60 was earned by Lisa
    tommy_fraction_of_lisa: float = 1/2 # Tommy earned half of what Lisa earned
):
    """Index: 36.
    Returns: the difference in earnings between Lisa and Tommy.
    """

    #: L1
    lisa_earned = total_earned * lisa_fraction

    #: L2

    #: L3
    difference = lisa_earned - total_earned

    #: FA
    answer = difference
    return answer