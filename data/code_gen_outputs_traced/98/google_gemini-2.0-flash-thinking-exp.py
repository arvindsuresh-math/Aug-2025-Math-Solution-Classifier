def solve(
    gumballs_to_todd: int = 4, # He gave 4 to Todd
    gumballs_remaining: int = 6 # If Hector had 6 gumballs remaining
):
    """Index: 98.
    Returns: the total number of gumballs Hector purchased.
    """

    #: L1
    gumballs_to_alisha = gumballs_to_todd * 2 # eval: 8 = 4 * 2

    #: L2
    gumballs_to_bobby = (gumballs_to_alisha * 4) - 5 # eval: 27 = (8 * 4) - 5

    #: L3
    total_purchased = gumballs_to_todd + gumballs_to_alisha + gumballs_to_bobby + gumballs_remaining # eval: 45 = 4 + 8 + 27 + 6

    #: FA
    answer = total_purchased
    return answer # eval: return 45
