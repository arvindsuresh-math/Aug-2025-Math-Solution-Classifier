def solve():
    """Index: 3681.
    Returns: the time it will take for the pot to be full in minutes.
    """
    # L1
    pot_volume_liters = 3 # 3 liters
    ml_per_liter = 1000 # WK
    pot_volume_ml = pot_volume_liters * ml_per_liter

    # L2
    drops_per_minute = 3 # 3 drops a minute
    ml_per_drop = 20 # Each drop is 20 ml
    ml_per_minute = drops_per_minute * ml_per_drop

    # L3
    time_to_fill_minutes = pot_volume_ml / ml_per_minute

    # FA
    answer = time_to_fill_minutes
    return answer