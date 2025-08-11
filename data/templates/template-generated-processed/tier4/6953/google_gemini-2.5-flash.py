def solve():
    """Index: 6953.
    Returns: the number of 5 ounce candles Haleigh can make.
    """
    # L1
    large_candle_oz = 20 # 20 oz candles
    original_wax_left_percent = 0.1 # 10% of it's original wax left
    wax_from_large_candle = large_candle_oz * original_wax_left_percent

    # L2
    num_large_candles = 5 # five 20 oz candles
    total_wax_from_large_candles = num_large_candles * wax_from_large_candle

    # L3
    medium_candle_oz = 5 # 5 five ounce candles
    wax_from_medium_candle = medium_candle_oz * original_wax_left_percent

    # L4
    num_medium_candles = 5 # 5 five ounce candles
    total_wax_from_medium_candles = num_medium_candles * wax_from_medium_candle

    # L5
    small_candle_oz = 1 # one ounce candles
    wax_from_small_candle = small_candle_oz * original_wax_left_percent

    # L6
    num_small_candles = 25 # twenty-five one ounce candles
    total_wax_from_small_candles = num_small_candles * wax_from_small_candle

    # L7
    total_wax_available = total_wax_from_large_candles + total_wax_from_medium_candles + total_wax_from_small_candles

    # L8
    new_candle_size_oz = 5 # 5 ounce candles
    num_new_candles = total_wax_available / new_candle_size_oz

    # FA
    answer = num_new_candles
    return answer