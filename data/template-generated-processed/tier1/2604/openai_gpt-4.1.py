def solve():
    """Index: 2604.
    Returns: the number of stickers Andrew kept.
    """
    # L1
    daniel_stickers = 250 # Daniel received 250 stickers
    fred_more_than_daniel = 120 # Fred received 120 more stickers than Daniel
    fred_stickers = daniel_stickers + fred_more_than_daniel

    # L2
    total_shared = daniel_stickers + fred_stickers

    # L3
    andrew_initial = 750 # Andrew bought 750 stickers
    andrew_kept = andrew_initial - total_shared

    # FA
    answer = andrew_kept
    return answer