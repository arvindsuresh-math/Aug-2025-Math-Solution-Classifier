def solve(
    pages_read_in_20_min: int = 8, # Joy can read 8 pages of a book in 20 minutes.
    time_interval_minutes: int = 20, # in 20 minutes
    pages_to_read: int = 120 # How many hours will it take her to read 120 pages?
):
    """Index: 14.
    Returns: the number of hours it will take Joy to read 120 pages.
    """

    #: L1
    minutes_in_an_hour = 60 # eval: 60 = 60
    sets_of_20_min_in_an_hour = minutes_in_an_hour / time_interval_minutes # eval: 3.0 = 60 / 20

    #: L2
    pages_read_per_hour = pages_read_in_20_min * sets_of_20_min_in_an_hour # eval: 24.0 = 8 * 3.0

    #: L3
    hours_to_read_120_pages = pages_to_read / pages_read_in_20_min # eval: 15.0 = 120 / 8

    #: FA
    answer = hours_to_read_120_pages
    return answer # eval: return 15.0
