def solve(
    pages_per_letter: int = 3,  # James writes a 3-page letter
    num_friends: int = 2,       # to 2 different friends
    times_per_week: int = 2     # twice a week
):
    """Index: 4.
    Returns: the total number of pages James writes in a year.
    """

    #: L1
    pages_per_friend_per_week = pages_per_letter * times_per_week

    #: L2
    total_pages_per_week = pages_per_friend_per_week * num_friends

    #: L3
    total_pages_per_year = total_pages_per_week * 52

    answer = total_pages_per_year  # FINAL ANSWER
    return answer