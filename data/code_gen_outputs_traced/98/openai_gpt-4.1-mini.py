def solve(
    gumballs_given_todd: int = 4,  # He gave 4 to Todd
    gumballs_remaining: int = 6    # Hector had 6 gumballs remaining
):
    """Index: 98.
    Returns: the total number of gumballs Hector originally purchased.
    """
    #: L1
    gumballs_given_alisha = gumballs_given_todd * 2 # eval: 8 = 4 * 2
    #: L2
    gumballs_given_bobby = (gumballs_given_alisha * 4) - 5 # eval: 27 = (8 * 4) - 5
    #: L3
    total_gumballs = gumballs_given_todd + gumballs_given_alisha + gumballs_given_bobby + gumballs_remaining # eval: 45 = 4 + 8 + 27 + 6
    answer = total_gumballs  # FINAL ANSWER # eval: 45 = 45  # FINAL ANSWER
    return answer # eval: return 45