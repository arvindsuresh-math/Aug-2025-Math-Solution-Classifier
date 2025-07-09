def solve(
    geckos_last_year: int = 86,  # Brandon sold 86 geckos last year
    multiplier: int = 2  # He sold twice that many the year before
):
    """Index: 88.
    Returns: the total number of geckos Brandon sold in the last two years."""

    #: L1

    #: L2
    geckos_two_years_ago = multiplier * multiplier

    #: L3
    total_geckos_sold = multiplier + geckos_two_years_ago

    #: FA
    answer = total_geckos_sold
    return answer