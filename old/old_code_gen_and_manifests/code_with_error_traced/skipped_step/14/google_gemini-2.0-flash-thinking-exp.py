def solve(
    pages_read_in_time: int = 8, # read 8 pages
    time_in_minutes: int = 20, # in 20 minutes
    total_pages_to_read: int = 120 # read 120 pages
):
    """Index: 14.
    Returns: the time in hours to read the specified number of pages.
    """

    #: L1
    minutes_in_hour = 60 # eval: 60 = 60
    intervals_in_hour = minutes_in_hour / time_in_minutes # eval: 3.0 = 60 / 20

    #: L2

    #: L3
    time_needed_hours = total_pages_to_read / time_in_minutes # eval: 6.0 = 120 / 20

    #: FA
    answer = time_needed_hours
    return answer # eval: return 6.0
