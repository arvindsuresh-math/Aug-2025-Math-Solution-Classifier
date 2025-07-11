def solve():
    """Index: 220.
    Returns: the number of additional gallons of gas Mr. Montero needs.
    """
    # L1
    distance_one_way = 600 # travel 600 miles, back and forth
    total_distance = distance_one_way + distance_one_way

    # L2
    miles_per_gallon_reference_distance = 400 # travel 400 miles
    sets_of_reference_distance = total_distance / miles_per_gallon_reference_distance

    # L3
    gallons_per_reference_distance = 20 # A car uses 20 gallons of gas
    total_gallons_needed = gallons_per_reference_distance * sets_of_reference_distance

    # L4
    gallons_in_car = 8 # Mr. Montero's car has 8 gallons in it
    gallons_to_add = total_gallons_needed - gallons_in_car

    # FA
    answer = gallons_to_add
    return answer