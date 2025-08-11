def solve():
    """Index: 6435.
    Returns: the total number of pages Jairus and Arniel read altogether.
    """
    # L1
    jairus_pages = 20 # 20 pages of the newspaper
    multiplier_twice = 2 # twice the number of pages
    twice_jairus_pages = jairus_pages * multiplier_twice

    # L2
    arniel_more = 2 # 2 more than twice the number of pages Jairus read
    arniel_pages = twice_jairus_pages + arniel_more

    # L3
    total_pages_read = jairus_pages + arniel_pages

    # FA
    answer = total_pages_read
    return answer