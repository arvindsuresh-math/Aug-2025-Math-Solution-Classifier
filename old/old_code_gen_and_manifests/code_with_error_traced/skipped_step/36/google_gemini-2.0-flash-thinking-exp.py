def solve(
    total_earnings: int = 60, # earned $60
    lisa_fraction: float = 1/2, # half of the $60 was earned by Lisa
    tommy_fraction_of_lisa: float = 1/2 # Tommy earned half of what Lisa earned
):
    """Index: 36.
    Returns: the difference in earnings between Lisa and Tommy.
    """

    #: L1
    lisa_earnings = total_earnings * lisa_fraction # eval: 30.0 = 60 * 0.5

    #: L2

    #: L3
    difference = lisa_earnings - tommy_fraction_of_lisa # eval: 29.5 = 30.0 - 0.5

    #: FA
    answer = difference
    return answer # eval: return 29.5
