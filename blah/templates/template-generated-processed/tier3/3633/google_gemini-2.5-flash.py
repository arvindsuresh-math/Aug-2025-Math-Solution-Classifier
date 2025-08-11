def solve():
    """Index: 3633.
    Returns: the total time in minutes to drink the whole bottle of water.
    """
    # L1
    bottle_volume_liters = 2 # 2-liter bottle
    ml_per_liter = 1000 # WK
    total_ml_in_bottle = bottle_volume_liters * ml_per_liter

    # L2
    ml_per_sip = 40 # each sip is 40 ml
    total_sips = total_ml_in_bottle / ml_per_sip

    # L3
    minutes_per_sip = 5 # every five minutes
    total_minutes = total_sips * minutes_per_sip

    # FA
    answer = total_minutes
    return answer