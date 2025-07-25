def solve():
    """Index: 4983.
    Returns: the number of hours Violet and her dog can spend hiking.
    """
    # L1
    violet_water_per_hour_ml = 800 # Violet needs 800 ml of water per hour hiked
    dog_water_per_hour_ml = 400 # her dog needs 400 ml of water per hour
    total_water_per_hour_ml = violet_water_per_hour_ml + dog_water_per_hour_ml

    # L2
    ml_per_liter = 1000 # WK
    total_water_per_hour_L = total_water_per_hour_ml / ml_per_liter

    # L3
    violet_carrying_capacity_L = 4.8 # Violet can carry 4.8 L of water
    hours_can_hike = violet_carrying_capacity_L / total_water_per_hour_L

    # FA
    answer = hours_can_hike
    return answer