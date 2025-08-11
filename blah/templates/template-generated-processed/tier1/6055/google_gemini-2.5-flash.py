def solve():
    """Index: 6055.
    Returns: how many more pages Cristobal read than Beatrix.
    """
    # L1
    pages_more_than_three_times = 15 # 15 more than three times
    multiplier_three_times = 3 # three times the pages
    beatrix_pages = 704 # Beatrix read 704 pages
    cristobal_pages = pages_more_than_three_times + multiplier_three_times * beatrix_pages

    # L2
    cristobal_more_than_beatrix = cristobal_pages - beatrix_pages

    # FA
    answer = cristobal_more_than_beatrix
    return answer