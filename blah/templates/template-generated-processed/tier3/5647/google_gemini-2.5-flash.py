def solve():
    """Index: 5647.
    Returns: the number of additional miles Carol can drive after getting home.
    """
    # L1
    trip_miles = 220 # 220 miles away
    miles_per_gallon = 20 # 20 miles to the gallon
    gallons_for_trip = trip_miles / miles_per_gallon

    # L2
    tank_capacity = 16 # 16-gallon gas tank
    remaining_gallons = tank_capacity - gallons_for_trip

    # L3
    extra_miles_after_home = remaining_gallons * miles_per_gallon

    # FA
    answer = extra_miles_after_home
    return answer