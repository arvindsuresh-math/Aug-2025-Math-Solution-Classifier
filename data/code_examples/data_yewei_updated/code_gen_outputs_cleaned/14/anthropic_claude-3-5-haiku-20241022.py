def solve(
    pages_read_in_20_mins: int = 8,  # Joy can read 8 pages in 20 minutes
    total_pages: int = 120,  # total pages to read
    minutes_per_set: int = 20  # 20 minutes per set
):
    """Index: 14.
    Returns: the number of hours needed to read the total pages."""
    #: L1
    sets_per_hour = 60 / minutes_per_set

    #: L2
    pages_read_per_hour = pages_read_in_20_mins * sets_per_hour

    #: L3
    hours_to_read = total_pages / pages_read_per_hour

    answer = hours_to_read  # FINAL ANSWER
    return answer