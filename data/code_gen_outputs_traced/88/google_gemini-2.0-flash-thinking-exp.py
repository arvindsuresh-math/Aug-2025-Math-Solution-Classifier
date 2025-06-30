def solve(
    geckos_last_year: int = 86 # Brandon sold 86 geckos last year
):
    """Index: 88.
    Returns: the total number of geckos sold in the last two years.
    """

    #: L2
    geckos_year_before = geckos_last_year * 2 # eval: 172 = 86 * 2

    #: L3
    total_geckos_sold = geckos_last_year + geckos_year_before # eval: 258 = 86 + 172

    #: FA
    answer = total_geckos_sold # eval: 258 = 258
    return answer # eval: return 258
