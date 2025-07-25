def solve():
    """Index: 5836.
    Returns: the number of ounces of wax Kellan has left.
    """
    # L1
    wax_for_car = 3 # 3 ounces of wax to detail Kellan’s car
    wax_for_suv = 4 # 4 ounces to detail his SUV
    total_wax_used_for_vehicles = wax_for_car + wax_for_suv

    # L2
    initial_bottle_size = 11 # an 11-ounce bottle of vehicle wax
    spilled_ounces = 2 # spilled 2 ounces
    wax_left = initial_bottle_size - spilled_ounces - total_wax_used_for_vehicles

    # FA
    answer = wax_left
    return answer