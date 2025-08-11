def solve():
    """Index: 282.
    Returns: the total number of stickers Riku has.
    """
    # L1
    kristoff_stickers = 85 # Kristoff has 85 stickers
    riku_multiplier = 25 # Riku has 25 times more stickers than Kristoff
    riku_extra_stickers = riku_multiplier * kristoff_stickers

    # L2
    riku_total_stickers = riku_extra_stickers + kristoff_stickers

    # FA
    answer = riku_total_stickers
    return answer