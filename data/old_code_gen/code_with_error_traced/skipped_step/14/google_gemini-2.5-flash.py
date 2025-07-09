def solve(
        pages_per_segment: int = 8, # read 8 pages
        minutes_per_segment: int = 20, # in 20 minutes
        target_pages: int = 120 # read 120 pages
    ):
    """Index: 14.
    Returns: the number of hours it will take to read the target number of pages.
    """

    #: L1

    #: L2
    pages_per_hour = pages_per_segment * pages_per_segment # eval: 64 = 8 * 8

    #: L3
    hours_to_read_target_pages = target_pages / pages_per_hour # eval: 1.875 = 120 / 64

    #: FA
    answer = hours_to_read_target_pages
    return answer # eval: return 1.875
