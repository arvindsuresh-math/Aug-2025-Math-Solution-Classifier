def solve(
    gumballs_to_todd: int = 4, # He gave 4 to Todd
    gumballs_remaining: int = 6, # Hector had 6 gumballs remaining
):
    """Index: 98.
    Returns: the total number of gumballs that Hector purchased.
    """

    #: L1
    gumballs_to_alisha = gumballs_remaining * 2 # eval: 12 = 6 * 2

    #: L2
    gumballs_to_bobby = (gumballs_to_alisha * 4) - 5 # eval: 43 = (12 * 4) - 5

    #: L3
    total_gumballs_purchased = gumballs_to_todd + gumballs_to_alisha + gumballs_to_bobby + gumballs_remaining # eval: 65 = 4 + 12 + 43 + 6

    #: FA
    answer = total_gumballs_purchased
    return answer # eval: return 65
