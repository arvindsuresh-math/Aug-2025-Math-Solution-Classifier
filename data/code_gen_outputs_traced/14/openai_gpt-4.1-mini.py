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
    pages_per_hour = pages_per_20_min * sets_per_hour # eval: 24.0 = 8 * 3.0
    #: L3
    hours_needed = total_pages / pages_per_hour # eval: 5.0 = 120 / 24.0
    answer = hours_needed  # FINAL ANSWER # eval: 5.0 = 5.0  # FINAL ANSWER
    return answer # eval: return 5.0