def solve():
    """Index: 3813.
    Returns: the number of candles Carmen will use.
    """
    # L1
    initial_burn_hours = 1 # Burning a candle for 1 hour
    initial_duration_nights = 8 # lasts her 8 nights
    new_burn_hours = 2 # burns the candle for 2 hours a night
    new_duration_nights = initial_duration_nights / new_burn_hours

    # L2
    total_nights_needed = 24 # over 24 nights
    candles_needed = total_nights_needed / new_duration_nights

    # FA
    answer = candles_needed
    return answer