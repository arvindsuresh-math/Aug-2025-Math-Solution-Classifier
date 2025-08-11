def solve():
    """Index: 6739.
    Returns: the combined weight of the candles in ounces.
    """
    # L1
    beeswax_per_candle = 8 # 8 ounces of beeswax
    coconut_oil_per_candle = 1 # 1 ounce of coconut oil
    weight_per_candle = beeswax_per_candle + coconut_oil_per_candle

    # L2
    total_candles_base = 10 # 10 candles
    candles_less = 3 # three less than 10 candles
    num_candles_made = total_candles_base - candles_less

    # L3
    combined_weight = num_candles_made * weight_per_candle

    # FA
    answer = combined_weight
    return answer