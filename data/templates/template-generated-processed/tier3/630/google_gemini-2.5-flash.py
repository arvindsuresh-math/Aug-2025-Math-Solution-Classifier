def solve():
    """Index: 630.
    Returns: the number of blue candles Avianna had.
    """
    # L1
    red_ratio_part = 5 # red candles and blue candles in the ratio of 5:3
    blue_ratio_part = 3 # red candles and blue candles in the ratio of 5:3
    total_ratio_parts = red_ratio_part + blue_ratio_part

    # L2
    red_candles = 45 # 45 red candles
    intermediate_product = total_ratio_parts * red_candles
    total_candles = intermediate_product / red_ratio_part

    # L3
    blue_candles = total_candles - red_candles

    # FA
    answer = blue_candles
    return answer