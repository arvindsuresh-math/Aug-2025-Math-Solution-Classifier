def solve(
    gumballs_given_to_todd: int = 4,  # Hector gave 4 to Todd
    gumballs_remaining: int = 6  # Hector had 6 gumballs remaining
):
    """Index: 98.
    Returns: the total number of gumballs Hector originally purchased.
    """
    #: L1
    gumballs_given_to_alisha = gumballs_given_to_todd * 2

    #: L2
    gumballs_given_to_bobby = (gumballs_given_to_alisha * 4) - 5

    #: L3
    total_gumballs_purchased = (
        gumballs_given_to_todd + 
        gumballs_given_to_alisha + 
        gumballs_given_to_bobby + 
        gumballs_remaining
    )

    answer = total_gumballs_purchased  # FINAL ANSWER
    return answer