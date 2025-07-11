def solve():
    """Index: 282.
    Returns: the total number of stickers Riku has.
    """
    # L1
    kristoff_stickers = 85 # Kristoff has 85 stickers
    riku_times_more = 25 # 25 times more stickers
    riku_more_stickers = riku_times_more * kristoff_stickers

    # L2
    total_riku_stickers = riku_more_stickers + kristoff_stickers

    # FA
    answer = total_riku_stickers
    return answer