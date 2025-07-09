def solve(
        gumballs_given_to_todd: int = 4, # He gave 4 to Todd
        gumballs_remaining: int = 6 # If Hector had 6 gumballs remaining
    ):
    """Index: 98.
    Returns: the total number of gumballs that Hector purchased.
    """

    #: L1
    gumballs_given_to_alisha = gumballs_given_to_todd * 2 # eval: 8 = 4 * 2

    #: L2
    gumballs_given_to_bobby = (gumballs_given_to_alisha * 4) - 5 # eval: 27 = (8 * 4) - 5

    #: L3
    total_gumballs_purchased = gumballs_given_to_todd * gumballs_given_to_alisha + gumballs_given_to_bobby + gumballs_remaining # eval: 65 = 4 * 8 + 27 + 6

    #: FA
    answer = total_gumballs_purchased
    return answer # eval: return 65
