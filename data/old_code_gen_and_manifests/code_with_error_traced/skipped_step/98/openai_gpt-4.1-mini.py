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

    #: L3
    total_gumballs = gumballs_given_todd + gumballs_given_alisha + gumballs_given_todd + gumballs_remaining # eval: 22 = 4 + 8 + 4 + 6

    #: FA
    answer = total_gumballs
    return answer # eval: return 22
