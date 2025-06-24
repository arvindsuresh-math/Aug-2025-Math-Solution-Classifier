def solve(
    last_year_sales: int = 86, # Brandon sold 86 geckos last year.
    multiplier_previous_year: int = 2 # He sold twice that many the year before.
):
    """Index: 88.
    Returns: the total number of geckos Brandon sold in the last two years.
    """
    #: L1
    # last_year_sales is already defined as an argument

    #: L2
    previous_year_sales = last_year_sales * multiplier_previous_year

    #: L3
    total_sales = last_year_sales + previous_year_sales

    answer = total_sales # FINAL ANSWER
    return answer