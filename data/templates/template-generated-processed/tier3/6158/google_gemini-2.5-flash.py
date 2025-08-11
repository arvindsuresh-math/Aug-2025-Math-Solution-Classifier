def solve():
    """Index: 6158.
    Returns: the total amount Joseph pays for the power used by these gadgets.
    """
    # L1
    oven_power_cost = 500 # power worth $500 in a month
    water_heater_divisor = 2 # twice what Joseph pays for the power the water heater uses
    water_heater_cost = oven_power_cost / water_heater_divisor

    # L2
    water_heater_and_oven_cost = water_heater_cost + oven_power_cost

    # L3
    refrigerator_multiplier = 3 # three times the amount he pays for the power used by the water heater
    refrigerator_cost = refrigerator_multiplier * water_heater_cost

    # L4
    total_cost = water_heater_and_oven_cost + refrigerator_cost

    # FA
    answer = total_cost
    return answer