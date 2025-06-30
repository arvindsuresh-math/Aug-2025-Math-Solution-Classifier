def solve(
    pages_read_in_20_mins: int = 8,  # Joy can read 8 pages in 20 minutes
    total_pages: int = 120,  # total pages to read
    minutes_per_hour: int = 60  # minutes in an hour
):
    """Index: 14.
    Returns: the number of hours needed to read the total pages."""

    #: L1
    sets_of_20_mins_per_hour = minutes_per_hour // 20

    #: L2
    pages_read_per_hour = pages_read_in_20_mins * sets_of_20_mins_per_hour

    #: L3

    #: FA
    answer = total_pages
    return answer