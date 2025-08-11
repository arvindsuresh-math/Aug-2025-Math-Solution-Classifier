def solve():
    """Index: 3513.
    Returns: the current cost for fuel.
    """
    # L1
    original_cost_per_tank = 200 # $200 to refill the tank
    price_increase_percent_decimal = 0.2 # went up by 20%
    cost_increase = original_cost_per_tank * price_increase_percent_decimal

    # L2
    new_cost_per_tank = original_cost_per_tank + cost_increase

    # L3
    fuel_capacity_multiplier = 2 # double fuel capacity
    total_cost_now = new_cost_per_tank * fuel_capacity_multiplier

    # FA
    answer = total_cost_now
    return answer