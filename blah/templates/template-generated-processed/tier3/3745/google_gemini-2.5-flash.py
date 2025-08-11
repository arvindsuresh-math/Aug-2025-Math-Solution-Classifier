def solve():
    """Index: 3745.
    Returns: the number of minutes it will take for the dish to be ready.
    """
    # L1
    final_temperature = 100 # 100 degrees before it is ready to eat
    initial_temperature = 20 # It is 20 degrees when she places it in the oven
    required_temperature_change = final_temperature - initial_temperature

    # L2
    heating_rate_per_minute = 5 # it heats up 5 degrees every minute
    cooking_time_minutes = required_temperature_change / heating_rate_per_minute

    # FA
    answer = cooking_time_minutes
    return answer