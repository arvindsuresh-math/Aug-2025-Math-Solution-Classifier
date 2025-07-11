def solve():
    """Index: 2604.
    Returns: the number of stickers Andrew kept.
    """
    # L1
    daniel_received = 250 # Daniel received 250 stickers
    fred_more_than_daniel = 120 # Fred received 120 more stickers than Daniel
    fred_received = daniel_received + fred_more_than_daniel

    # L2
    total_shared = daniel_received + fred_received

    # L3
    andrew_bought_total = 750 # Andrew bought 750 stickers
    andrew_kept = andrew_bought_total - total_shared

    # FA
    answer = andrew_kept
    return answer