def solve(
    pages_per_20_min: int = 8,  # Joy can read 8 pages in 20 minutes
    total_pages: int = 120      # total pages to read
):
    """Index: 14.
    Returns: the number of hours it will take Joy to read the total pages.
    """

    #: L1
    sets_per_hour = 60 / 20 # eval: 3.0 = 60 / 20

    #: L2
    pages_per_hour = pages_per_20_min + sets_per_hour # eval: 11.0 = 8 + 3.0

    #: L3
    hours_needed = total_pages / pages_per_hour # eval: 10.909090909090908 = 120 / 11.0

    #: FA
    answer = hours_needed
    return answer # eval: return 10.909090909090908
