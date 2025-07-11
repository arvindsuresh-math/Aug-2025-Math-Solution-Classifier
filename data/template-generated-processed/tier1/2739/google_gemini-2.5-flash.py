def solve():
    """Index: 2739.
    Returns: the total value of gold Legacy and Aleena have together.
    """
    # L1
    legacy_bars = 5 # Legacy has 5 bars of gold
    aleena_fewer_than_legacy = 2 # 2 bars fewer than she has
    aleena_bars = legacy_bars - aleena_fewer_than_legacy

    # L2
    total_bars = legacy_bars + aleena_bars

    # L3
    value_per_bar = 2200 # a bar of gold is worth $2200
    total_value = total_bars * value_per_bar

    # FA
    answer = total_value
    return answer