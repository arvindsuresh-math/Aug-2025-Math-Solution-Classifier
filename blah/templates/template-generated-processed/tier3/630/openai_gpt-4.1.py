def solve():
    """Index: 630.
    Returns: the number of blue candles Avianna had.
    """
    # L1
    red_ratio = 5 # ratio of red candles
    blue_ratio = 3 # ratio of blue candles
    total_ratio = red_ratio + blue_ratio

    # L2
    red_candles = 45 # Avianna had 45 red candles
    total_candles = (total_ratio * red_candles) / red_ratio

    # L3
    blue_candles = total_candles - red_candles

    # FA
    answer = blue_candles
    return answer