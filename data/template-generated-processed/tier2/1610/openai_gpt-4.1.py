def solve():
    """Index: 1610.
    Returns: the total liters of water Micah drank from morning until afternoon.
    """
    # L1
    morning_liters = 1.5 # Micah drank 1.5 liters of water in the morning
    afternoon_multiplier = 3 # three times that much water in the afternoon
    afternoon_liters = morning_liters * afternoon_multiplier

    # L2
    total_liters = morning_liters + afternoon_liters

    # FA
    answer = total_liters
    return answer