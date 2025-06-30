def solve(
    pages_read_in_20_mins: int = 8,  # Joy can read 8 pages in 20 minutes
    total_pages: int = 120,  # total pages to read
    minutes_per_hour: int = 60  # minutes in an hour
):
    """Index: 14.
    Returns: the number of hours needed to read the total pages."""
    #: L1
    sets_of_20_mins_per_hour = minutes_per_hour // 20 # eval: 3 = 60 // 20
    #: L2
    pages_read_per_hour = pages_read_in_20_mins * sets_of_20_mins_per_hour # eval: 24 = 8 * 3
    #: L3
    hours_to_read = total_pages / pages_read_per_hour # eval: 5.0 = 120 / 24
    answer = hours_to_read  # FINAL ANSWER # eval: 5.0 = 5.0  # FINAL ANSWER
    return answer # eval: return 5.0