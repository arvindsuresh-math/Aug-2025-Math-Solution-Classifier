def solve():
    """Index: 88.
    Returns: the total number of geckos Brandon sold in the last two years.
    """
    # L2
    geckos_last_year = 86 # sold 86 geckos last year
    multiplier_twice = 2 # sold twice that many
    geckos_two_years_ago = geckos_last_year * multiplier_twice

    # L3
    total_geckos_sold = geckos_last_year + geckos_two_years_ago

    # FA
    answer = total_geckos_sold
    return answer