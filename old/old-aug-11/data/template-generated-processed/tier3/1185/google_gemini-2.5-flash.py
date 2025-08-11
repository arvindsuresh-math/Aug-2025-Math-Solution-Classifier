def solve():
    """Index: 1185.
    Returns: the total kilograms of tomatoes needed.
    """
    # L1
    total_tomatoes_for_3_liters = 69 # 69 kg of tomatoes
    liters_for_69_kg = 3 # 3 liters of ketchup
    tomatoes_per_liter = total_tomatoes_for_3_liters / liters_for_69_kg

    # L2
    desired_liters = 5 # make 5 liters of ketchup
    total_tomatoes_needed = tomatoes_per_liter * desired_liters

    # FA
    answer = total_tomatoes_needed
    return answer