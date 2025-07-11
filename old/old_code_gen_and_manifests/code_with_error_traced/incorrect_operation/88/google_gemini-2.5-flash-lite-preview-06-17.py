def solve(
    last_year_sales: int = 86, # Brandon sold 86 geckos last year.
    multiplier_previous_year: int = 2 # He sold twice that many the year before.
):
    """Index: 88.
    Returns: the total number of geckos Brandon sold in the last two years.
    """

    #: L2
    previous_year_sales = last_year_sales + multiplier_previous_year # eval: 88 = 86 + 2

    #: L3
    total_sales = last_year_sales + previous_year_sales # eval: 174 = 86 + 88

    #: FA
    answer = total_sales
    return answer # eval: return 174
