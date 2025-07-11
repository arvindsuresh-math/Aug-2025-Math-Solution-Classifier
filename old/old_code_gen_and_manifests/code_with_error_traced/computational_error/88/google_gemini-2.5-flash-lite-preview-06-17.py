def solve(
    last_year_sales: int = 86, # Brandon sold 86 geckos last year.
    multiplier_previous_year: int = 2 # He sold twice that many the year before.
):
    """Index: 88.
    Returns: the total number of geckos Brandon sold in the last two years.
    """

    #: L2
    previous_year_sales = 162 # eval: 162 = 162

    #: L3
    total_sales = last_year_sales + previous_year_sales # eval: 248 = 86 + 162

    #: FA
    answer = total_sales
    return answer # eval: return 248
