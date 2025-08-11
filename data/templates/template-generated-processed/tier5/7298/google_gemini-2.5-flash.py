def solve():
    """Index: 7298.
    Returns: the fuel consumption of the car per 100 km.
    """
    # L1
    initial_gasoline = 47 # contains 47 liters of gasoline
    gasoline_left = 14 # 14 liters left
    distance_traveled = 275 # journey of 275 km
    gasoline_consumed = initial_gasoline - gasoline_left

    # L4
    target_distance = 100 # WK
    numerator_for_x = gasoline_consumed * target_distance
    fuel_consumption_per_100km = numerator_for_x / distance_traveled

    # FA
    answer = fuel_consumption_per_100km
    return answer