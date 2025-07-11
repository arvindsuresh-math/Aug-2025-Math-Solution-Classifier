def solve():
    """Index: 4.
    Returns: the number of pages James writes in a year.
    """
    # L1
    pages_per_letter = 3  # a 3-page letter
    times_per_week = 2  # twice a week
    pages_per_friend_per_week = pages_per_letter * times_per_week

    # L2
    num_friends = 2  # 2 different friends
    total_pages_per_week = pages_per_friend_per_week * num_friends

    # L3
    weeks_per_year = 52  # WK
    pages_per_year = total_pages_per_week * weeks_per_year

    # FA
    answer = pages_per_year
    return answer