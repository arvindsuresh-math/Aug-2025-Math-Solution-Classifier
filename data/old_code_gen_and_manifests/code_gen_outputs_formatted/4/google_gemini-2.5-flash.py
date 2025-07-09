def solve(
        pages_per_letter: int = 3, # a 3-page letter
        num_friends: int = 2, # to 2 different friends
        times_per_week: int = 2, # twice a week
        weeks_per_year: int = 52 # (implicit: number of weeks in a year)
    ):
    """Index: 4.
    Returns: the total number of pages James writes in a year.
    """

    #: L1
    pages_per_friend_per_week = pages_per_letter * times_per_week

    #: L2
    total_pages_per_week = pages_per_friend_per_week * num_friends

    #: L3
    total_pages_per_year = total_pages_per_week * weeks_per_year

    #: FA
    answer = total_pages_per_year
    return answer