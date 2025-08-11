def solve():
    """Index: 88.
    Returns: the total number of geckos Brandon sold in the last two years.
    """
    # L2
    last_year = 86 # Brandon sold 86 geckos last year
    multiplier = 2 # twice that many the year before
    year_before = last_year * multiplier

    # L3
    total_geckos = last_year + year_before

    # FA
    answer = total_geckos
    return answer