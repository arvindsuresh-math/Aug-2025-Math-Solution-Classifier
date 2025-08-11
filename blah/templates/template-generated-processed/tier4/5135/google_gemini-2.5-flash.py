def solve():
    """Index: 5135.
    Returns: Kerry's age.
    """
    # L1
    total_candle_cost = 5 # If the candles cost $5
    cost_per_box = 2.5 # $2.5 a box
    num_boxes = total_candle_cost / cost_per_box

    # L2
    candles_per_box = 12 # Candles come in boxes of 12
    total_candles = num_boxes * candles_per_box

    # L3
    num_cakes = 3 # three cakes
    kerry_age = total_candles / num_cakes

    # FA
    answer = kerry_age
    return answer