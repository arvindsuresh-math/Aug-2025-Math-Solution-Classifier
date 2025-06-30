def solve(
    total_earned: int = 60,  # Lisa, Jack, and Tommy earned $60
):
    """Index: 36.
    Returns: how much more money Lisa earned than Tommy.
    """
    #: L1
    lisa_earned = total_earned * 1/2 # eval: 30.0 = 60 * 1/2
    #: L2
    tommy_earned = lisa_earned * 1/2 # eval: 15.0 = 30.0 * 1/2
    #: L3
    difference = lisa_earned - tommy_earned # eval: 15.0 = 30.0 - 15.0
    answer = difference  # FINAL ANSWER # eval: 15.0 = 15.0  # FINAL ANSWER
    return answer # eval: return 15.0