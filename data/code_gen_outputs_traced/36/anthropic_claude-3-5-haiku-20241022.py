def solve(
    total_earnings: int = 60,  # Lisa, Jack, and Tommy earned $60 from washing cars
    lisa_fraction: float = 1/2,  # half of the $60 was earned by Lisa
    tommy_fraction: float = 1/2  # Tommy earned half of what Lisa earned
):
    """Index: 36.
    Returns: the difference in earnings between Lisa and Tommy."""
    #: L1
    lisa_earnings = total_earnings * lisa_fraction # eval: 30.0 = 60 * 0.5
    #: L2
    tommy_earnings = lisa_earnings * tommy_fraction # eval: 15.0 = 30.0 * 0.5
    #: L3
    earnings_difference = lisa_earnings - tommy_earnings # eval: 15.0 = 30.0 - 15.0
    answer = earnings_difference  # FINAL ANSWER # eval: 15.0 = 15.0  # FINAL ANSWER
    return answer # eval: return 15.0