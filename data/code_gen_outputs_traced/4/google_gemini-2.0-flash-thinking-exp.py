def solve(
    pages_per_letter: int = 3, # writes a 3-page letter
    num_friends: int = 2, # to 2 different friends
    times_per_week: int = 2, # twice a week
    weeks_per_year: int = 52 # (Implicit: number of weeks in a year)
):
    """Index: 4.
    Returns: the total number of pages James writes in a year.
    """

    #: L1
    pages_per_friend_per_week = pages_per_letter * times_per_week # eval: 6 = 3 * 2

    #: L2
    total_pages_per_week = pages_per_friend_per_week * num_friends # eval: 12 = 6 * 2

    #: L3
    total_pages_per_year = total_pages_per_week * weeks_per_year # eval: 624 = 12 * 52

    #: FA
    answer = total_pages_per_year # eval: 624 = 624
    return answer # eval: return 624
