def solve(
        geckos_last_year: int = 86, # Brandon sold 86 geckos last year
        multiplier_year_before: int = 2 # He sold twice that many the year before
    ):
    """Index: 88.
    Returns: the total number of geckos Brandon sold in the last two years.
    """
    #: L1
    # geckos_last_year is already defined by the argument

    #: L2
    geckos_two_years_ago = geckos_last_year * multiplier_year_before

    #: L3
    total_geckos_sold = geckos_last_year + geckos_two_years_ago

    answer = total_geckos_sold # FINAL ANSWER
    return answer