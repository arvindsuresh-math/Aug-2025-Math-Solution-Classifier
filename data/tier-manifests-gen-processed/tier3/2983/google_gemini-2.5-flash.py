def solve():
    """Index: 2983.
    Returns: the number of days Jacob needs to fill his water tank.
    """
    # L1
    rain_ml_per_day = 800 # 800 milliliters of water from the rain
    river_ml_per_day = 1700 # 1700 milliliters of water from the river
    total_ml_per_day = rain_ml_per_day + river_ml_per_day

    # L2
    tank_capacity_liters = 50 # 50 liters of water
    ml_per_liter = 1000 # WK
    tank_capacity_ml = tank_capacity_liters * ml_per_liter

    # L3
    days_to_fill_tank = tank_capacity_ml / total_ml_per_day

    # FA
    answer = days_to_fill_tank
    return answer