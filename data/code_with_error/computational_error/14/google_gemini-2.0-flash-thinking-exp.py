def solve(
    pages_read_in_time: int = 8, # read 8 pages
    time_in_minutes: int = 20, # in 20 minutes
    total_pages_to_read: int = 120 # read 120 pages
):
    """Index: 14.
    Returns: the time in hours to read the specified number of pages.
    """

    #: L1
    minutes_in_hour = 60
    intervals_in_hour = minutes_in_hour / time_in_minutes

    #: L2
    pages_per_hour = 25.0

    #: L3
    time_needed_hours = total_pages_to_read / pages_per_hour

    #: FA
    answer = time_needed_hours
    return answer