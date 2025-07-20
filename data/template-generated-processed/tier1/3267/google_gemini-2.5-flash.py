def solve():
    """Index: 3267.
    Returns: the number of blue candles used.
    """
    # L1
    yellow_candles = 27 # 27 yellow candles
    red_candles = 14 # 14 red candles
    yellow_and_red_candles = yellow_candles + red_candles

    # L2
    grandfather_age = 79 # turning 79 years old
    blue_candles = grandfather_age - yellow_and_red_candles

    # FA
    answer = blue_candles
    return answer