def solve():
    """Index: 687.
    Returns: the number of additional candles Stephanie needs.
    """
    # L1
    total_cupcakes = 24 # 24 cupcakes
    half_divisor = 2 # WK
    candles_per_cupcake_half1 = 1 # 1 candle each
    candles_for_half1 = (total_cupcakes / half_divisor) * candles_per_cupcake_half1

    # L2
    candles_per_cupcake_half2 = 2 # 2 candles each
    candles_for_half2 = (total_cupcakes / half_divisor) * candles_per_cupcake_half2

    # L3
    total_candles_needed = candles_for_half1 + candles_for_half2

    # L4
    candles_currently_has = 30 # currently has a total of 30 candles
    additional_candles_needed = total_candles_needed - candles_currently_has

    # FA
    answer = additional_candles_needed
    return answer