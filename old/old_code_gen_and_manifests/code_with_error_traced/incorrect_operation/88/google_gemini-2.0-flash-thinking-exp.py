def solve(
    geckos_last_year: int = 86 # Brandon sold 86 geckos last year
):
    """Index: 88.
    Returns: the total number of geckos sold in the last two years.
    """

    #: L2
    geckos_year_before = geckos_last_year - 2 # eval: 84 = 86 - 2

    #: L3
    total_geckos_sold = geckos_last_year + geckos_year_before # eval: 170 = 86 + 84

    #: FA
    answer = total_geckos_sold
    return answer # eval: return 170
