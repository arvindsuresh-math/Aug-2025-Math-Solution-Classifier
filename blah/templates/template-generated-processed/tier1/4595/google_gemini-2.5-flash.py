def solve():
    """Index: 4595.
    Returns: the total number of pages of novels read in a year.
    """
    # L1
    num_novels = 4 # 4 novels
    pages_per_novel = 200 # 200 pages each
    pages_per_month = num_novels * pages_per_novel

    # L2
    months_per_year = 12 # WK
    pages_per_year = pages_per_month * months_per_year

    # FA
    answer = pages_per_year
    return answer