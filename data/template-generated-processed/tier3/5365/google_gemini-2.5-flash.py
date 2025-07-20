def solve():
    """Index: 5365.
    Returns: the number of hives needed to make the target number of candles.
    """
    # L1
    total_candles_initial = 12 # 12 candles
    num_hives_initial = 3 # 3 beehives
    candles_per_hive = total_candles_initial / num_hives_initial

    # L2
    target_candles = 96 # 96 candles
    hives_needed = target_candles / candles_per_hive

    # FA
    answer = hives_needed
    return answer