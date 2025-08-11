def solve():
    """Index: 2012.
    Returns: the total number of stickers Ryan, Steven, and Terry have altogether.
    """
    # L1
    ryan_stickers = 30 # Ryan has 30 stickers
    steven_multiplier = 3 # Steven has thrice as many stickers as Ryan
    steven_stickers = steven_multiplier * ryan_stickers

    # L2
    terry_more_than_steven = 20 # Terry has 20 more stickers than Steven
    terry_stickers = steven_stickers + terry_more_than_steven

    # L3
    total_stickers = ryan_stickers + steven_stickers + terry_stickers

    # FA
    answer = total_stickers
    return answer