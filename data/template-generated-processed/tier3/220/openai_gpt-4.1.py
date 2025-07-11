def solve():
    """Index: 220.
    Returns: the number of additional gallons Mr. Montero needs to travel 600 miles back and forth.
    """
    # L1
    one_way_distance = 600 # 600 miles
    total_distance = one_way_distance + one_way_distance

    # L2
    miles_per_set = 400 # 400 miles
    sets_needed = total_distance / miles_per_set

    # L3
    gallons_per_set = 20 # 20 gallons of gas to travel 400 miles
    total_gallons_needed = gallons_per_set * sets_needed

    # L4
    current_gallons = 8 # Mr. Montero's car has 8 gallons in it
    gallons_to_add = total_gallons_needed - current_gallons

    # FA
    answer = gallons_to_add
    return answer