def solve(
    last_year_sales: int = 86, # Brandon sold 86 geckos last year.
    multiplier_previous_year: int = 2 # He sold twice that many the year before.
):
    """Index: 88.
    Returns: the total number of geckos Brandon sold in the last two years.
    """

    #: L2
    previous_year_sales = last_year_sales * multiplier_previous_year # eval: 172 = 86 * 2

    #: L3
    total_sales = last_year_sales + previous_year_sales # eval: 258 = 86 + 172

    #: FA
    answer = total_sales # eval: 258 = 258
    return answer # eval: return 258
