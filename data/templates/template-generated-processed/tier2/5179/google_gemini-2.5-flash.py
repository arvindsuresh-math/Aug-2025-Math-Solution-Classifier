def solve():
    """Index: 5179.
    Returns: the total weight of the tank with water.
    """
    # L1
    tank_capacity = 200 # The tank can hold 200 gallons
    fill_percentage = 0.8 # fills it to 80% of capacity
    water_gallons = tank_capacity * fill_percentage

    # L2
    weight_per_gallon = 8 # If a gallon of water weighs 8 pounds
    water_weight = water_gallons * weight_per_gallon

    # L3
    empty_tank_weight = 80 # It weighs 80 pounds empty
    total_weight = water_weight + empty_tank_weight

    # FA
    answer = total_weight
    return answer