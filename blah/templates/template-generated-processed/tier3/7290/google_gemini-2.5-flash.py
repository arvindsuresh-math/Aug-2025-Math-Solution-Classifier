def solve():
    """Index: 7290.
    Returns: the number of restaurants in the building.
    """
    # L1
    total_units = 300 # A building has 300 units
    half_divisor = 2 # Half the units are residential and the other half
    units_for_offices_and_restaurants = total_units / half_divisor

    # L2
    split_evenly_divisor = 2 # split evenly between offices and restaurants
    num_restaurants = units_for_offices_and_restaurants / split_evenly_divisor

    # FA
    answer = num_restaurants
    return answer