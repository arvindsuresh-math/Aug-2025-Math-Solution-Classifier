def solve(
    total_earned: int = 60,  # Lisa, Jack, and Tommy earned $60
):
    """Index: 36.
    Returns: how much more money Lisa earned than Tommy.
    """

    #: L1
    lisa_earned = total_earned * 1/2 # eval: 30.0 = 60 * 1/2

    #: L2
    tommy_earned = 16.0 # eval: 16.0 = 16.0

    #: L3
    difference = lisa_earned - tommy_earned # eval: 14.0 = 30.0 - 16.0

    #: FA
    answer = difference
    return answer # eval: return 14.0
