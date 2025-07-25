def solve():
    """Index: 2020.
    Returns: the total number of oysters Bob can shuck.
    """
    # L1
    minutes_per_hour = 60 # WK
    minutes_per_shuck_unit = 5 # 5 minutes
    five_minute_units_per_hour = minutes_per_hour / minutes_per_shuck_unit

    # L2
    oysters_in_5_minutes = 10 # 10 oysters
    oysters_per_hour = oysters_in_5_minutes * five_minute_units_per_hour

    # L3
    target_hours = 2 # in 2 hours
    total_oysters_shucked = target_hours * oysters_per_hour

    # FA
    answer = total_oysters_shucked
    return answer