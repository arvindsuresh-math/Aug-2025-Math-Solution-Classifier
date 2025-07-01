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
    pages_per_hour = pages_per_20_min * total_pages # eval: 960 = 8 * 120

    #: L3
    hours_needed = total_pages / pages_per_hour # eval: 0.125 = 120 / 960

    #: FA
    answer = hours_needed
    return answer # eval: return 0.125
