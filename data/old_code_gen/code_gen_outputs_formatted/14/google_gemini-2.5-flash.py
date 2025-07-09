def solve(
        pages_per_segment: int = 8, # read 8 pages
        minutes_per_segment: int = 20, # in 20 minutes
        target_pages: int = 120 # read 120 pages
    ):
    """Index: 14.
    Returns: the number of hours it will take to read the target number of pages.
    """

    #: L1
    sets_of_minutes_in_hour = 60 / minutes_per_segment

    #: L2
    pages_per_hour = pages_per_segment * sets_of_minutes_in_hour

    #: L3
    hours_to_read_target_pages = target_pages / pages_per_hour

    #: FA
    answer = hours_to_read_target_pages
    return answer