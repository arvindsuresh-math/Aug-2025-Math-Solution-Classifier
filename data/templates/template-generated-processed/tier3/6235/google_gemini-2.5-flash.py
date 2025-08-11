def solve():
    """Index: 6235.
    Returns: the total liters of gasoline Samson will need for a one-way trip.
    """
    # L1
    total_distance = 140 # 140 km away
    distance_per_unit_gas = 70 # 70 km
    number_of_gas_units = total_distance / distance_per_unit_gas

    # L2
    liters_per_unit = 10 # ten liters of gasoline
    total_gasoline_needed = number_of_gas_units * liters_per_unit

    # FA
    answer = total_gasoline_needed
    return answer