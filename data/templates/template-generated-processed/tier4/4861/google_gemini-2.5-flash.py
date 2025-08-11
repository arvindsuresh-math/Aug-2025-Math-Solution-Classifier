def solve():
    """Index: 4861.
    Returns: the time it will take Amalia to read 18 pages in minutes.
    """
    # L1
    time_taken_L1 = 2 # 2 minutes
    pages_read_L1 = 4 # 4 pages of her book
    time_per_page = time_taken_L1 / pages_read_L1

    # L2
    pages_to_read_L2 = 18 # 18 pages of her book
    total_time = pages_to_read_L2 * time_per_page

    # FA
    answer = total_time
    return answer