def solve():
    """Index: 3624.
    Returns: the number of additional gallons of gas needed.
    """
    # L1
    miles_per_gallon = 3 # 3 miles per gallon of gas
    gallons_in_tank = 12 # 12 gallons of gas in his tank
    miles_from_current_gas = miles_per_gallon * gallons_in_tank

    # L2
    total_distance_needed = 90 # 90 miles away
    remaining_miles_needed = total_distance_needed - miles_from_current_gas

    # L3
    gallons_needed = remaining_miles_needed / miles_per_gallon

    # FA
    answer = gallons_needed
    return answer