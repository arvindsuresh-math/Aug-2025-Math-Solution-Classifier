def solve():
    """Index: 6486.
    Returns: the total gallons of gas used.
    """
    # L1
    dermatologist_distance = 30 # 30 miles east from home to see her dermatologist
    round_trip_multiplier = 2 # and back home again
    dermatologist_round_trip_distance = dermatologist_distance * round_trip_multiplier

    # L2
    gynecologist_distance = 50 # 50 miles west from home to see her gynecologist
    gynecologist_round_trip_distance = gynecologist_distance * round_trip_multiplier

    # L3
    total_distance = dermatologist_round_trip_distance + gynecologist_round_trip_distance

    # L4
    miles_per_gallon = 20 # her car gets 20 miles per gallon
    gallons_of_gas = total_distance / miles_per_gallon

    # FA
    answer = gallons_of_gas
    return answer