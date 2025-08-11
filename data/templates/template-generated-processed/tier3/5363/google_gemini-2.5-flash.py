def solve():
    """Index: 5363.
    Returns: the total number of hours to drink 3 liters of water.
    """
    # L1
    goal_liters = 3 # 3 liters of water
    ml_per_liter = 1000 # WK
    goal_ml = goal_liters * ml_per_liter

    # L2
    ml_per_drink_session = 500 # 500 milliliters of water
    num_drink_sessions = goal_ml / ml_per_drink_session

    # L3
    hours_per_session = 2 # every after 2 hours
    total_hours = num_drink_sessions * hours_per_session

    # FA
    answer = total_hours
    return answer