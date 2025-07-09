def solve(
    pages_read_in_20_min: int = 8, # Joy can read 8 pages of a book in 20 minutes.
    time_interval_minutes: int = 20, # in 20 minutes
    pages_to_read: int = 120 # How many hours will it take her to read 120 pages?
):
    """Index: 14.
    Returns: the number of hours it will take Joy to read 120 pages.
    """

    #: L1
    minutes_in_an_hour = 60
    sets_of_20_min_in_an_hour = minutes_in_an_hour / time_interval_minutes

    #: L2
    pages_read_per_hour = pages_read_in_20_min * sets_of_20_min_in_an_hour

    #: L3
    hours_to_read_120_pages = pages_to_read / pages_read_per_hour

    #: FA
    answer = hours_to_read_120_pages
    return answer