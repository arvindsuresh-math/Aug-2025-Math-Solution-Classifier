def solve():
    """Index: 5757.
    Returns: the fuel consumption in 90 hours.
    """
    # L5
    initial_hours = 21 # In 21 hours
    initial_fuel = 7 # consumes 7 liters of fuel
    target_hours = 90 # in 90 hours
    intermediate_product_of_hours_fuel = target_hours * initial_fuel
    consumption_in_90_hours = intermediate_product_of_hours_fuel / initial_hours

    # FA
    answer = consumption_in_90_hours
    return answer