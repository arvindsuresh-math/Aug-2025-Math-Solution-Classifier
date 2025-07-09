def solve(
    geckos_last_year: int = 86  # Brandon sold 86 geckos last year
):
    """Index: 88.
    Returns: the total number of geckos Brandon sold in the last two years.
    """

    #: L2
    geckos_two_years_ago = geckos_last_year * 2 # eval: 172 = 86 * 2

    #: L3
    total_geckos_sold = geckos_two_years_ago + geckos_two_years_ago # eval: 344 = 172 + 172

    #: FA
    answer = total_geckos_sold
    return answer # eval: return 344
