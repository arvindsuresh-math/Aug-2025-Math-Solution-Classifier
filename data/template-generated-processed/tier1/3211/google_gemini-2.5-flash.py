def solve():
    """Index: 3211.
    Returns: the total pages Coral read in the 3 nights.
    """
    # L1
    pages_night_1 = 30 # 30 pages of a book on night 1

    # L2
    multiplier_night_2 = 2 # twice that
    less_night_2 = 2 # 2 less than twice that
    pages_night_2 = multiplier_night_2 * pages_night_1 - less_night_2

    # L3
    more_night_3 = 3 # 3 more pages
    pages_night_3 = more_night_3 + (pages_night_1 + pages_night_2)

    # L4
    total_pages = pages_night_1 + pages_night_2 + pages_night_3

    # FA
    answer = total_pages
    return answer