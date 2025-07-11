def solve():
    """Index: 4.
    Returns: the total number of pages James writes in a year.
    """
    # L1
    pages_per_letter = 3 # 3-page letter
    num_friends = 2 # 2 different friends
    pages_per_week_per_time = pages_per_letter * num_friends

    # L2
    times_per_week = 2 # twice a week
    pages_per_week = pages_per_week_per_time * times_per_week

    # L3
    weeks_per_year = 52 # WK
    pages_per_year = pages_per_week * weeks_per_year

    # FA
    answer = pages_per_year
    return answer